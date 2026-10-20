# tests/test_insight_cache.py
"""
==================================================
IFA — Intelligent Fitness Assistant

File: test_insight_cache.py

Purpose:
Regression tests for the /analytics/insights cache policy in
ai_insight_service.generate_insights().

Bug being locked down: a fallback result (Gemini failed) used
to be cached for the full 6 hours, so users kept seeing
fallback insights long after Gemini recovered.

Policy under test:
- AI-generated results: cached 6 hours (cost control, unchanged).
- Fallback results: cached only 5 minutes — long enough that an
  outage does not make every page load wait out the 20s Gemini
  timeout, short enough that AI insights return soon after recovery.

Time is simulated by moving the cached entry's timestamp back,
so no test sleeps.

==================================================
"""

from datetime import timedelta

import pytest

from app.schemas.insight import AIInsight, AIInsightList
from app.services import ai_insight_service as svc
from app.services.gemini_service import AIUnavailableError

CALLS = []


async def _gemini_down(prompt, structured_model=None, timeout=20):
    CALLS.append("down")
    raise AIUnavailableError("simulated outage")


async def _gemini_up(prompt, structured_model=None, timeout=20):
    CALLS.append("up")
    return AIInsightList(
        insights=[
            AIInsight(category="general", priority="low", title="AI insight", evidence="e", recommendation="r")
        ]
    )


@pytest.fixture(autouse=True)
def reset_calls():
    CALLS.clear()


def _age_cache_entry(user_id, delta):
    svc._insight_cache[user_id]["ts"] -= delta


def _get(client, headers):
    r = client.get("/analytics/insights", headers=headers)
    assert r.status_code == 200
    return r.json()["source"]


def test_fallback_is_retried_after_five_minutes_and_recovers_to_ai(client, make_user, auth_headers, monkeypatch):
    user = make_user()
    headers = auth_headers(user)

    monkeypatch.setattr(svc, "safe_invoke", _gemini_down)
    assert _get(client, headers) == "fallback"

    monkeypatch.setattr(svc, "safe_invoke", _gemini_up)  # Gemini is back
    _age_cache_entry(user.id, timedelta(minutes=6))
    assert _get(client, headers) == "ai"


def test_fallback_is_still_cached_inside_the_short_window(client, make_user, auth_headers, monkeypatch):
    user = make_user()
    headers = auth_headers(user)

    monkeypatch.setattr(svc, "safe_invoke", _gemini_down)
    assert _get(client, headers) == "fallback"

    monkeypatch.setattr(svc, "safe_invoke", _gemini_up)
    _age_cache_entry(user.id, timedelta(minutes=4))
    assert _get(client, headers) == "fallback"
    assert CALLS == ["down"]  # no second Gemini attempt during an outage burst


def test_ai_result_is_still_cached_for_six_hours(client, make_user, auth_headers, monkeypatch):
    user = make_user()
    headers = auth_headers(user)
    monkeypatch.setattr(svc, "safe_invoke", _gemini_up)

    assert _get(client, headers) == "ai"
    _age_cache_entry(user.id, timedelta(hours=5, minutes=59))
    assert _get(client, headers) == "ai"
    assert CALLS == ["up"]  # still served from cache

    _age_cache_entry(user.id, timedelta(minutes=2))  # now past 6h
    assert _get(client, headers) == "ai"
    assert CALLS == ["up", "up"]  # regenerated once


def test_cache_entry_from_before_this_change_still_works(client, make_user, auth_headers, monkeypatch):
    """An entry without a 'ttl' key (shape used before this change) must not crash."""
    user = make_user()
    headers = auth_headers(user)
    monkeypatch.setattr(svc, "safe_invoke", _gemini_up)
    assert _get(client, headers) == "ai"
    svc._insight_cache[user.id].pop("ttl", None)
    assert _get(client, headers) == "ai"
    assert CALLS == ["up"]
