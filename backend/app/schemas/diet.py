# app/schemas/diet.py
"""
==================================================
IFA — Intelligent Fitness Assistant

File: diet.py

Purpose:
Defines Pydantic schemas used for diet analysis,
calorie calculations and AI meal planning.

Functionality:
- Validates diet-related user inputs.
- Defines BMI response structures.
- Defines BMR response structures.
- Defines TDEE response structures.
- Defines macronutrient response structures.
- Defines meal plan request formats.
- Defines grocery list request formats.
- Standardizes data exchanged between backend and frontend.

Data Models:
DietInput
BMIResponse
BMRResponse
TDEEResponse
MacroResponse
MealPlanRequest
GroceryRequest

Used By:
diet_service.py
diet.py router
Dietician page

==================================================
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class DietInput(BaseModel):
    age: int = Field(gt=0)
    gender: str  # "male" | "female" | "non-binary"
    weight: float = Field(gt=0)
    height: float = Field(gt=0)
    activity_level: str


class BMIResponse(BaseModel):
    bmi: float
    category: str


class BMRResponse(BaseModel):
    bmr: float


class TDEEResponse(BaseModel):
    tdee: float


class MacroResponse(BaseModel):
    protein: float
    carbs: float
    fats: float


class MealPlanRequest(BaseModel):
    # Bounds keep absurd values (and unbounded free text) out of the Gemini
    # prompt. age matches the Profile page's own 10-120 cap.
    age: int = Field(gt=0, le=120)
    gender: str = Field(min_length=1, max_length=30)  # "male" | "female" | "non-binary"
    weight: float = Field(gt=0, le=500)
    height: float = Field(gt=0, le=300)
    goal: str = Field(min_length=1, max_length=100)
    diet_type: str = Field(min_length=1, max_length=100)

    # Optional — populated from the user's Profile when available (activity
    # level, and the calorie_goal already computed by profile_service's
    # calculate_targets()). Neither is required, so requests from users
    # without a saved profile behave exactly as before.
    activity_level: Optional[str] = Field(default=None, max_length=50)
    target_calories: Optional[int] = Field(default=None, gt=0, le=10000)


class GroceryRequest(BaseModel):
    meal_plan: str = Field(min_length=1, max_length=10000)

    # Optional — when the caller already has a persisted MealPlan (every
    # generated plan is persisted, see /diet/meal-plan), pass its id so the
    # generated grocery list is saved back onto that row instead of being
    # lost the moment the user navigates away. Omitted ⇒ today's stateless
    # behaviour is unchanged.
    plan_id: Optional[int] = None


class MealPlanResponse(BaseModel):
    id: int
    user_id: int
    goal: str
    diet_type: str
    meal_plan: str
    grocery_list: Optional[str] = None
    # Optional — defensive against any pre-existing row whose created_at was
    # inserted NULL before app/models/meal_plan.py gained its Python-side
    # default (see that file for why the DB-side server_default alone
    # wasn't reliably applied on the live table). New rows always populate
    # this now; this just stops an old row from turning a whole
    # /diet/history response into a 500.
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True
