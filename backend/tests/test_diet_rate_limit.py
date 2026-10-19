# tests/test_diet_rate_limit.py
"""
==================================================
IFA — Intelligent Fitness Assistant

File: test_diet_rate_limit.py

Purpose:
Regression tests for the rate limits and input bounds on the
two Gemini-backed Dietician routes, POST /diet/meal-plan and
POST /diet/grocery-list.

Gemini is stubbed at the call sites diet.py imports, same as
test_dietician_persistence.py, so no network is involved.

Tests:
- meal-plan: 5 requests succeed, the 6th is a 429.
- grocery-list: 10 requests succeed, the 11th is a 429.
- The limit is per user (token), not shared: one user hitting
  the limit does not block another.
- An unauthenticated request is still a 401, never a 429/500.
- Out-of-range / oversized request bodies are a 422 and never
  reach Gemini; an ordinary request is unaffected.

==================================================
"""

import pytest

GEMINI_CALLS = []


async def _fake_meal_plan(**kwargs):
    GEMINI_CALLS.append("meal_plan")
    return "Breakfast:\n- oats"


async def _fake_grocery(meal_plan):
    GEMINI_CALLS.append("grocery")
    return "- oats"


@pytest.fixture(autouse=True)
def stub_gemini(monkeypatch):
    GEMINI_CALLS.clear()
    monkeypatch.setattr("app.routers.diet.generate_meal_plan", _fake_meal_plan)
    monkeypatch.setattr("app.routers.diet.generate_grocery_list", _fake_grocery)


def _payload(**overrides):
    body = {
        "age": 28,
        "gender": "male",
        "weight": 70,
        "height": 175,
        "goal": "Muscle Gain",
        "diet_type": "Vegetarian",
    }
    body.update(overrides)
    return body


def test_meal_plan_is_limited_to_five_per_minute(client, make_user, auth_headers):
    headers = auth_headers(make_user())
    codes = [client.post("/diet/meal-plan", json=_payload(), headers=headers).status_code for _ in range(6)]
    assert codes == [200, 200, 200, 200, 200, 429]
    assert len(GEMINI_CALLS) == 5  # the rejected request never reached Gemini


def test_grocery_list_is_limited_to_ten_per_minute(client, make_user, auth_headers):
    headers = auth_headers(make_user())
    codes = [
        client.post("/diet/grocery-list", json={"meal_plan": "Breakfast: oats"}, headers=headers).status_code
        for _ in range(11)
    ]
    assert codes == [200] * 10 + [429]


def test_limit_is_per_user_not_shared(client, make_user, auth_headers):
    a = make_user(username="a", email="a@example.com")
    b = make_user(username="b", email="b@example.com")
    for _ in range(5):
        assert client.post("/diet/meal-plan", json=_payload(), headers=auth_headers(a)).status_code == 200
    assert client.post("/diet/meal-plan", json=_payload(), headers=auth_headers(a)).status_code == 429
    assert client.post("/diet/meal-plan", json=_payload(), headers=auth_headers(b)).status_code == 200


def test_unauthenticated_request_is_401_not_429(client):
    codes = {client.post("/diet/meal-plan", json=_payload()).status_code for _ in range(8)}
    assert codes == {401}


@pytest.mark.parametrize(
    "overrides",
    [
        {"age": 0},
        {"age": 121},
        {"weight": 501},
        {"height": 301},
        {"goal": ""},
        {"goal": "x" * 101},
        {"diet_type": "x" * 101},
        {"gender": "x" * 31},
        {"activity_level": "x" * 51},
        {"target_calories": 0},
        {"target_calories": 10001},
    ],
)
def test_invalid_meal_plan_body_is_422_and_never_reaches_gemini(client, make_user, auth_headers, overrides):
    r = client.post("/diet/meal-plan", json=_payload(**overrides), headers=auth_headers(make_user()))
    assert r.status_code == 422
    assert GEMINI_CALLS == []


def test_oversized_or_empty_grocery_body_is_422(client, make_user, auth_headers):
    headers = auth_headers(make_user())
    assert client.post("/diet/grocery-list", json={"meal_plan": "x" * 10001}, headers=headers).status_code == 422
    assert client.post("/diet/grocery-list", json={"meal_plan": ""}, headers=headers).status_code == 422
    assert GEMINI_CALLS == []


def test_what_the_dietician_page_sends_still_works(client, make_user, auth_headers):
    # The page posts numbers as strings from <input>, plus optional profile context.
    body = _payload(age="25", weight="70.5", height="175", activity_level="moderate", target_calories=2200)
    r = client.post("/diet/meal-plan", json=body, headers=auth_headers(make_user()))
    assert r.status_code == 200
