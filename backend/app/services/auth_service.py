# app/services/auth_service.py
"""
==================================================
IFA — Intelligent Fitness Assistant

File: auth_service.py

Purpose:
Provides authentication utilities for user
security, password management and JWT handling.

Functionality:
- Hashes user passwords.
- Verifies passwords.
- Creates JWT access tokens.
- Authenticates users.
- Retrieves the current authenticated user.
- Loads authentication environment variables.

Responsibilities:
Password security
JWT token generation
User authentication
Protected route access

Used By:
auth.py router
All protected routes
JWT authentication system

==================================================
"""

import os
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from jose import jwt, JWTError
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User

load_dotenv()

# Secrets that are publicly known — committed in this repo's .env.example, or
# used as the old hard-coded fallback. A deployment signing tokens with one of
# these would let anyone forge a login, so startup refuses them.
_KNOWN_PUBLIC_SECRETS = frozenset(
    {
        "change_this_to_a_secure_random_secret_key_32bytes_plus",
        "fallback_dev_secret_key_change_in_production",
    }
)


def _load_secret_key(raw):
    """
    Returns the JWT signing key, or raises RuntimeError if it is missing,
    blank, or a known public placeholder.

    The value is returned EXACTLY as given — never stripped. Stripping would
    change the HMAC key and invalidate every token already issued.
    """
    if raw is None or not raw.strip():
        raise RuntimeError("SECRET_KEY environment variable must be set")
    if raw.strip() in _KNOWN_PUBLIC_SECRETS:
        raise RuntimeError(
            "SECRET_KEY is set to a publicly known placeholder. Generate a real "
            'one: python -c "import secrets; print(secrets.token_urlsafe(48))"'
        )
    return raw


SECRET_KEY = _load_secret_key(os.getenv("SECRET_KEY"))

ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise credentials_exception

    return user
