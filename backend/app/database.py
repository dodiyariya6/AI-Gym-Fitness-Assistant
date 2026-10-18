# app/database.py
"""
==================================================
IFA — Intelligent Fitness Assistant

File: database.py

Purpose:
Configures the database connection and
SQLAlchemy session management.

Functionality:
- Loads environment variables.
- Establishes the Neon PostgreSQL connection.
- Creates the SQLAlchemy engine.
- Configures database sessions.
- Defines the Base model.
- Provides database sessions to API routes.

Responsibilities:
Database configuration
Session management
Connection handling
ORM initialization

Used By:
All models
All routers
All services

==================================================
"""

from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, declarative_base

from dotenv import load_dotenv

import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Pin the Postgres driver explicitly. A bare "postgresql://" URL lets
# SQLAlchemy pick the default driver, and that default changed between
# versions (psycopg2 in 2.0.x, psycopg v3 in 2.1+). We ship psycopg2-binary,
# so name it here. URLs that already name a driver (e.g. +psycopg) and
# non-Postgres URLs (e.g. the SQLite URL used by the tests) are left alone.
# This must run BEFORE create_engine() below.
if DATABASE_URL:
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql+psycopg2://", 1)
    elif DATABASE_URL.startswith("postgresql://"):
        DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+psycopg2://", 1)


engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=300,
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()


def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()
