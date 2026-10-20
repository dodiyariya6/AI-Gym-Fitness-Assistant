# tests/test_secret_key.py
"""
==================================================
IFA — Intelligent Fitness Assistant

File: test_secret_key.py

Purpose:
Regression tests for startup validation of SECRET_KEY
(auth_service._load_secret_key).

Why these tests call the function directly instead of
re-importing auth_service: the module also calls
load_dotenv(), so on a developer machine with a real
backend/.env an "unset" import test would silently pick
the key up from that file and pass or fail depending on
who runs it.

Tests:
- Unset, empty and whitespace-only keys are rejected.
- Every publicly known placeholder is rejected, including
  the value currently in backend/.env.example (read from
  the file so the test cannot drift from it).
- A real key is returned byte-for-byte unchanged — never
  stripped, or every issued token would stop verifying.
- The key the test suite itself uses is accepted.

==================================================
"""

import pathlib

import pytest

from app.services.auth_service import _load_secret_key

ENV_EXAMPLE = pathlib.Path(__file__).resolve().parents[1] / ".env.example"


def _env_example_secret() -> str:
    for line in ENV_EXAMPLE.read_text().splitlines():
        if line.startswith("SECRET_KEY="):
            return line.split("=", 1)[1]
    raise AssertionError("SECRET_KEY line missing from backend/.env.example")


@pytest.mark.parametrize("bad", [None, "", "   ", "\n", "\t "])
def test_missing_or_blank_secret_is_rejected(bad):
    with pytest.raises(RuntimeError, match="must be set"):
        _load_secret_key(bad)


def test_env_example_placeholder_is_rejected():
    with pytest.raises(RuntimeError, match="publicly known"):
        _load_secret_key(_env_example_secret())


def test_old_hardcoded_fallback_is_rejected():
    with pytest.raises(RuntimeError, match="publicly known"):
        _load_secret_key("fallback_dev_secret_key_change_in_production")


def test_placeholder_with_stray_whitespace_is_rejected():
    # A copy-paste into a hosting dashboard commonly adds a trailing newline.
    with pytest.raises(RuntimeError, match="publicly known"):
        _load_secret_key(_env_example_secret() + "\n")


def test_real_secret_is_returned_unchanged_including_whitespace():
    secret = "k3y-with-trailing-newline-0123456789abcdef\n"
    assert _load_secret_key(secret) == secret


def test_secret_used_by_the_test_suite_is_accepted():
    assert _load_secret_key("pytest-test-secret-key") == "pytest-test-secret-key"
