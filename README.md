<div align="center">

# IFA — Intelligent Fitness Assistant

### A personal AI-powered fitness, nutrition, and wellness platform

Track workouts and daily habits, train with browser-based pose detection, create nutrition plans, discover nearby gyms, and understand your progress through connected analytics and AI-assisted coaching.

[![React](https://img.shields.io/badge/React-19-61DAFB?style=for-the-badge&logo=react&logoColor=111827)](https://react.dev/)
[![Vite](https://img.shields.io/badge/Vite-8-646CFF?style=for-the-badge&logo=vite&logoColor=white)](https://vite.dev/)
[![FastAPI](https://img.shields.io/badge/FastAPI-REST_API-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Neon-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Gemini](https://img.shields.io/badge/Google_Gemini-AI-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-Pose_Landmarker-0097A7?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/edge/mediapipe/solutions/vision/pose_landmarker)
[![pytest](https://img.shields.io/badge/pytest-Backend_Tests-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://pytest.org/)

[Live Application](https://ai-gym-fitness-assistant-beta.vercel.app) · [Backend API](https://ai-gym-fitness-assistant-e2rv.onrender.com) · [Interactive API Docs](https://ai-gym-fitness-assistant-e2rv.onrender.com/docs) · [Source Code](https://github.com/dodiyariya6/AI-Gym-Fitness-Assistant)

</div>

---

## Contents

- [Project at a Glance](#project-at-a-glance)
- [Live Demo](#live-demo)
- [Screenshots](#screenshots)
- [What IFA Does](#what-ifa-does)
- [Application Modules](#application-modules)
  - [Dashboard](#1-dashboard)
  - [Profile and Personalised Targets](#2-profile-and-personalised-targets)
  - [Workout Tracker](#3-workout-tracker)
  - [Browser-Based Webcam Trainer](#4-browser-based-webcam-trainer)
  - [Habit Tracker](#5-habit-tracker)
  - [AI Dietician](#6-ai-dietician)
  - [AI Fitness Coach](#7-ai-fitness-coach)
  - [Reports and Analytics](#8-reports-and-analytics)
  - [Consistency and Achievements](#9-consistency-and-achievements)
  - [Gym Finder](#10-gym-finder)
- [System Architecture](#system-architecture)
- [Request and Data Flow](#request-and-data-flow)
- [AI Design and Reliability](#ai-design-and-reliability)
- [Technology Stack](#technology-stack)
- [Repository Structure](#repository-structure)
- [Database Model Overview](#database-model-overview)
- [API Overview](#api-overview)
- [Authentication and Security](#authentication-and-security)
- [Getting Started](#getting-started)
- [Environment Variables](#environment-variables)
- [Running the Application](#running-the-application)
- [Testing](#testing)
- [Deployment](#deployment)
- [Known Limitations](#known-limitations)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

---

## Project at a Glance

IFA is a full-stack fitness application designed to bring workout tracking, daily wellness habits, nutrition planning, exercise-form feedback, gym discovery, and fitness analytics into one connected experience.

The application is built around a shared user account and a common data store. Workout records, habit logs, profile information, saved meal plans, and analytics can therefore be used across relevant modules rather than being treated as unrelated features.

A central design principle is to **calculate measurable results in application code and use AI to interpret or generate content where it adds value**. The wellness score, nutrition calculations, trend analysis, and other deterministic results are computed by backend logic. Google Gemini is used for AI-assisted insights, conversational coaching, and generated nutrition content.

### Project links

| Resource | Link |
|---|---|
| Web application | [ai-gym-fitness-assistant-beta.vercel.app](https://ai-gym-fitness-assistant-beta.vercel.app) |
| Backend API | [ai-gym-fitness-assistant-e2rv.onrender.com](https://ai-gym-fitness-assistant-e2rv.onrender.com) |
| Interactive API documentation | [OpenAPI / Swagger UI](https://ai-gym-fitness-assistant-e2rv.onrender.com/docs) |
| GitHub repository | [dodiyariya6/AI-Gym-Fitness-Assistant](https://github.com/dodiyariya6/AI-Gym-Fitness-Assistant) |

### Deployment components

| Layer | Technology / service |
|---|---|
| Frontend hosting | Vercel |
| Backend hosting | Render |
| Relational database | Neon PostgreSQL |
| AI provider | Google Gemini |
| Maps and gym discovery data | OpenStreetMap ecosystem |

> **Note:** Live availability depends on the hosting platforms, database connectivity, API quotas, and external service availability. The public links identify the configured deployments; they are not a guarantee that every external integration is available at every moment.

---

## Live Demo

Open the [IFA web application](https://ai-gym-fitness-assistant-beta.vercel.app).

The backend exposes interactive API documentation at [`/docs`](https://ai-gym-fitness-assistant-e2rv.onrender.com/docs). The documentation is generated by FastAPI from the routes and schemas registered by the running backend.

For a first-time walkthrough, the intended order is:

1. Register or sign in.
2. Complete the profile so the application has the information needed for personalisation.
3. Log a few workouts and daily habits.
4. Open the Dashboard and Reports to see the available metrics.
5. Try the AI Dietician and AI Fitness Coach.
6. Open the Webcam Trainer and grant camera access when prompted.
7. Try Gym Finder with location permission or the profile-location fallback.

The amount of visible analytics depends on the records available to the signed-in account. A new account with no history will naturally show less historical information than an account with logged workouts and habits.

---

## Screenshots

The repository contains the screenshots listed below under `screenshots/`. They are embedded directly from the repository so they can be viewed from the GitHub README.

> **Screenshot note:** These are the image files currently committed to the repository. Some screenshots may represent an earlier UI state than the currently deployed application. Use the live application to verify the latest layout and interactions.

### 1. Dashboard

The Dashboard brings together key fitness and wellness information for a quick overview.

![IFA Dashboard](screenshots/dashboard-hero.png)

### 2. Dashboard Analytics

A closer view of the analytics area and summary metrics.

![Dashboard Analytics](screenshots/dashboard-analytics.png)

### 3. Workout Tracker

The Workout Tracker records exercise sessions and makes the saved workout history available to the rest of the application.

![Workout Tracker](screenshots/workout-tracker.png)

### 4. Habit Tracker

The Habit Tracker records daily wellness inputs such as sleep, hydration, steps, and workout completion.

![Habit Tracker](screenshots/habit-tracker.png)

### 5. AI Dietician

The Dietician interface supports AI-assisted meal planning and nutrition-related workflows.

![AI Dietician](screenshots/dietician-mealplan.png)

### 6. AI Fitness Coach

The conversational coach provides a chat interface for fitness-related questions and guidance.

![AI Fitness Coach](screenshots/fitness-chat.png)

### 7. Webcam Trainer

The Webcam Trainer provides the exercise-session interface for browser-based pose analysis.

![Webcam Trainer](screenshots/webcam-trainer.png)

### 8. Live Pose Detection

This screenshot illustrates the webcam pose-detection experience.

![Webcam Live Pose Detection](screenshots/webcam-live-detection.png)

### 9. Reports and Insights

The Reports page presents a deeper view of progress and analytics.

![Reports and Insights](screenshots/reports-overview.png)

### 10. Gym Finder

Gym Finder combines nearby gym results with location-based discovery.

![Gym Finder](screenshots/gym-fnder.png)

> The filename `gym-fnder.png` is intentionally written as it exists in the repository. Do not rename the reference unless the image file itself is renamed.

### 11. Profile

The Profile page stores the personal and fitness information used by relevant features.

![Profile](screenshots/profile.png)

---

## What IFA Does

IFA groups fitness workflows into a single application:

- **Track activity:** Save manual workouts and completed webcam workout sessions.
- **Record habits:** Maintain daily sleep, water-intake, steps, and workout-completion logs.
- **Personalise the experience:** Use profile information and fitness goals in relevant targets and calculations.
- **Plan nutrition:** Calculate common nutrition metrics and request AI-generated meal plans and grocery lists.
- **Ask for coaching:** Use a conversational fitness assistant with bounded recent chat history and fitness context.
- **Analyse progress:** Review wellness scoring, trends, consistency, progressive overload, and habit/workout associations.
- **Discover gyms:** Search nearby gym listings using location data and map services.
- **Track milestones:** View consistency information and achievement progress.

The modules are connected through the authenticated user and backend services. Not every feature depends on AI: core calculations and stored records remain application responsibilities.

---

## Application Modules

### 1. Dashboard

The Dashboard is the application's summary view. It combines selected workout, habit, wellness, consistency, and insight information so the user can review their current state without opening every module.

Depending on the data available, the dashboard can show:

- Workout and activity summaries.
- Habit-related metrics.
- A wellness score and its component breakdown.
- Consistency and achievement information.
- A compact selection of generated or fallback insights.
- Navigation to the detailed Reports page and other modules.

The dashboard should be interpreted as a summary, not as a separate data source. Its metrics are produced from the backend's saved records and analytics services.

### 2. Profile and Personalised Targets

The Profile module stores the information used to personalise supported features. This includes relevant biometric information, fitness goals, activity level, and location.

Profile information is used by backend profile and diet services to support calculations and targets such as:

- Water-intake targets.
- Sleep targets.
- Step targets.
- Calorie-related targets.
- Nutrition calculations based on the available profile data.
- A fallback location for Gym Finder when browser geolocation is not used.

Personalised targets are calculated by application logic. They should not be confused with measurements from a wearable device or with medical advice.

### 3. Workout Tracker

The Workout Tracker supports manual workout logging and saved sessions created by the Webcam Trainer.

Workout records can include fields such as:

- Exercise name.
- Repetitions.
- Sets or duration, depending on the record and form.
- Date.
- Notes.
- Form score when available.
- Estimated calories when calculated for the session.

The backend workout service estimates calories using a MET-based calculation and the user's available body-weight information. If the required profile weight is unavailable, the current implementation uses a fallback weight of 70 kg. Consequently, calorie values are estimates rather than direct measurements.

Saved workouts feed the workout history and relevant analytics. The backend checks record ownership for supported operations.

### 4. Browser-Based Webcam Trainer

The Webcam Trainer performs pose detection in the user's browser using **MediaPipe Tasks Vision**. It does not rely on the deployed backend opening a physical camera.

Supported exercise counters in the current frontend include:

- Squats.
- Bicep curls.
- Pushups.
- Lunges.
- Jumping jacks.

The browser requests camera permission, loads the pose-landmarker model and vision assets, processes video frames, and uses client-side exercise-counter logic to track repetitions and derive a form score. When the session finishes, the application sends the workout summary to the existing backend workout-save flow.

#### Webcam processing flow

1. The user opens Webcam Trainer and selects an exercise.
2. The browser requests camera access through `getUserMedia()`.
3. MediaPipe Tasks Vision loads its WASM assets and pose-landmarker model.
4. Video frames are analysed in the browser.
5. The exercise counter estimates repetitions and session metrics.
6. The application calculates the session summary, including the form score and estimated calories.
7. The summary is saved as a workout through the backend.

**Video privacy boundary:** The current frontend implementation processes camera frames locally and submits the resulting workout summary for persistence; it does not send the live video frames to the IFA backend. MediaPipe's model and WASM assets are loaded from external CDNs, so the browser still needs network access to those resources.

#### Browser requirements

- A modern browser that supports `getUserMedia()`.
- Camera permission.
- HTTPS in deployment or `localhost` during local development.
- Network access to load MediaPipe assets and its model.
- A functioning camera device.

Camera access can fail if permission is denied, no camera is available, another application is using the camera, or the browser is not in a secure context.

Pose-based repetition and form scoring are software estimates. They are not a substitute for professional coaching, injury assessment, or medical evaluation.

### 5. Habit Tracker

The Habit Tracker stores daily wellness logs. The supported fields include:

- Water intake.
- Sleep hours.
- Steps.
- Workout-completion status.
- Date.

The module supports reviewing logs and presenting habit information over time. Habit records are used by analytics and consistency logic, so the history shown in one part of the application can affect summaries shown elsewhere.

The current service checks for an existing log for the same user and date before creating another entry. This application-level check should not be interpreted as a database-enforced guarantee against simultaneous duplicate requests; database constraints and concurrency handling are separate concerns.

### 6. AI Dietician

The Dietician combines deterministic nutrition calculations with AI-generated content.

#### Deterministic calculations

The backend provides endpoints and service logic for:

- **BMI:** Body mass index from available height and weight.
- **BMR:** Basal metabolic rate using the Mifflin–St Jeor equation.
- **TDEE:** An estimated daily energy expenditure based on BMR and the selected activity level.
- **Macronutrient calculations:** Derived nutrition targets from the supplied inputs and application rules.

These calculations depend on the accuracy and completeness of the input data.

#### AI-generated nutrition content

The Dietician can request Gemini to generate:

- Personalised meal-plan content.
- Grocery-list content associated with a plan.

Generated plans are saved by the backend. The Recent Plans workflow can retrieve a saved plan without requiring the user to generate it again. The UI separates loading an existing plan from requesting a new one.

AI-generated nutrition content is general informational guidance. It should not be treated as a clinical diet, a diagnosis, or a replacement for advice from a qualified nutrition professional.

If the AI provider is unavailable, nutrition-generation endpoints may report an unavailable-service response instead of returning a newly generated plan.

### 7. AI Fitness Coach

The AI Fitness Coach provides a conversational interface for fitness-related questions.

The backend assembles a bounded fitness context from available application data. Depending on the service and available records, that context can include workout summaries, habit summaries, wellness metrics, trends, and relevant findings.

Conversation sessions and messages are persisted. The service sends a limited recent-history window to the AI model rather than an unlimited lifetime transcript, helping control prompt size and keep recent context relevant.

When Gemini cannot produce a reply, the service has a fallback response path. A fallback reply should not be mistaken for a fresh AI-generated recommendation.

The coach is intended for general fitness information and habit support. It is not a medical diagnostic tool.

### 8. Reports and Analytics

Reports provides a deeper view than the compact Dashboard summary. It surfaces analytics and structured insight information produced by backend services.

The analytics layer includes logic for:

- Aggregated workout metrics.
- Habit metrics.
- Recent rolling habit summaries.
- Wellness-score calculation and component breakdown.
- Trend directions where comparison data exists.
- Progressive-overload classification.
- Habit/workout association analysis.
- Fitness insights that can be displayed in Dashboard and Reports.

#### Wellness score

The wellness score is a 0–100 application metric. The current backend breakdown allocates up to 100 points across these components:

| Component | Maximum points | What it represents |
|---|---:|---|
| Sleep | 25 | Sleep-hours input and the configured sleep threshold |
| Water intake | 20 | Water-intake input relative to the configured target |
| Steps | 15 | Step count relative to the configured threshold |
| Workout completion | 10 | Recent habit-logging coverage used by the current implementation |
| Form score | 20 | Average saved form score when available |
| Streak | 10 | Current habit-logging streak band |
| **Total** | **100** | **Sum of the component values** |

The score is an application-defined indicator, not a validated medical or scientific health score. Missing data can reduce the score because the implementation cannot award points for values that have not been recorded.

**Implementation detail:** The component currently labelled `workout_completion` uses the number of distinct days with habit logs in the recent seven-day window to calculate its rate. It does not independently prove that a workout was completed on each of those days. This distinction matters when interpreting the score.

#### Progressive overload

The progressive-overload service evaluates recorded workout sessions by exercise. It compares averages from earlier and later portions of the available session history and classifies the trend when enough data exists. The current logic requires a minimum of three sessions before making a classification and also considers inactivity.

The result is an indicator derived from the logged sessions, not a guarantee that a user has gained muscle or strength. Missing or inconsistent exercise names, reps, or session history can limit the reliability of the comparison.

#### Habit/workout associations

The correlation service analyses available habit and workout data and can use Pearson's correlation coefficient when the sample requirements are met. A correlation is an association, not proof that one habit caused a workout outcome. Sparse or inconsistent logs can make the result unavailable or unstable.

### 9. Consistency and Achievements

The Consistency module reports activity patterns and habit-logging continuity over supported time windows. The Achievements module evaluates configured milestone rules and stores user achievement progress.

These features are based on application records. A missing log can affect a streak or milestone even if the activity happened in real life but was not entered into IFA.

### 10. Gym Finder

Gym Finder discovers nearby gym listings using the OpenStreetMap ecosystem and related public services.

The frontend can use browser geolocation when permission is granted. The profile's saved city/location can be used as a fallback when browser location is unavailable. The search interface supports a configurable radius and presents results on an interactive map.

The relevant technologies include:

- **Nominatim** for geocoding supported location text.
- **Overpass API** for querying mapped gym-related objects.
- **OpenStreetMap** for map tiles and geographic data.
- **Leaflet / React Leaflet** for interactive map rendering.

Results depend on the completeness of OpenStreetMap data and the availability and usage limits of the public services. A missing result does not prove that no gym exists in an area.

---

## System Architecture

```mermaid
flowchart TD
    U[User / Browser] --> FE[React + Vite Frontend]
    FE --> AUTH[Authentication and Protected Routes]
    FE --> API[FastAPI REST API]
    FE --> CAM[Browser Webcam Trainer]
    CAM --> MP[MediaPipe Tasks Vision]
    CAM --> SAVE[Workout Summary]
    SAVE --> API
    API --> ROUTERS[API Routers]
    ROUTERS --> SERVICES[Backend Services]
    SERVICES --> DB[(Neon PostgreSQL)]
    SERVICES --> ANALYTICS[Deterministic Analytics]
    SERVICES --> AI[Gemini Integration]
    EXT[OpenStreetMap / Nominatim / Overpass] <--> SERVICES
    ANALYTICS --> INSIGHTS[Computed Findings]
    INSIGHTS --> AI
    AI --> RESPONSE[AI Content / Coach Replies]
    DB --> RESPONSE
    RESPONSE --> FE
```

### Architectural responsibilities

| Layer | Responsibility |
|---|---|
| React frontend | Pages, navigation, form interactions, charts, maps, browser camera access, and API calls |
| Frontend services | HTTP requests to the backend, grouped by feature |
| FastAPI routers | HTTP endpoints, request handling, authentication dependencies, and response construction |
| Pydantic schemas | Request/response data validation and serialization |
| Backend services | Business rules, calculations, persistence workflows, AI orchestration, and external-service calls |
| SQLAlchemy models | Python representation of persisted database entities |
| Neon PostgreSQL | Persistent application data |
| Gemini integration | AI-assisted interpretation, chat responses, and generated nutrition content |
| MediaPipe in browser | Local pose detection and exercise-session analysis |
| OpenStreetMap ecosystem | Geographic data used by gym discovery |

The architecture separates the browser-based pose-processing path from the backend's data-persistence path. The backend receives the final workout summary rather than the camera stream.

---

## Request and Data Flow

### Standard authenticated request

1. The user interacts with a page in the React application.
2. The relevant frontend service sends an HTTP request using the shared Axios client.
3. The backend router validates the request and applies authentication where required.
4. The router calls the appropriate service.
5. The service reads or writes database records and performs any required calculations.
6. The backend returns a response.
7. The frontend updates the page and renders the returned state.

### Analytics and AI-insight flow

1. The backend reads the user's saved profile, workout records, and habit records.
2. Deterministic services compute metrics and findings.
3. A compact context is assembled from the available data.
4. The insight service may ask Gemini to interpret those findings.
5. The service validates the returned structure and uses fallback logic where supported.
6. Dashboard and Reports display the resulting metrics and insights.

The AI model is not the source of truth for the numeric analytics. The relevant backend services compute those values.

### Nutrition flow

1. The Dietician collects or pre-fills the relevant user inputs.
2. Deterministic endpoints calculate supported metrics such as BMI, BMR, TDEE, and macros.
3. A meal-plan or grocery-list request is sent to the backend.
4. The backend calls Gemini when configured and available.
5. The generated content is returned and saved as a meal-plan record where supported.
6. The user can retrieve saved plans from plan history.

---

## AI Design and Reliability

IFA uses Gemini for tasks where natural-language generation is useful, while keeping deterministic application calculations in backend code.

### Deterministic application logic

The backend computes the following without requiring Gemini to invent numeric results:

- Wellness-score components and total.
- Supported workout and habit aggregates.
- Trend directions where comparison data exists.
- Progressive-overload classifications.
- Habit/workout association statistics.
- BMI, BMR, TDEE, and macro calculations.
- Consistency and achievement rules.

### AI-assisted functionality

Gemini is used for:

- Interpreting existing analytics findings into user-facing insights.
- Conversational fitness-coach replies.
- Generating meal-plan content.
- Generating grocery-list content.

### Context boundaries

The fitness context service prepares a compact representation of relevant user data for supported AI workflows. The purpose is to supply useful context without sending an unbounded database history. Context can be limited by the available records and by the history bounds implemented by each service.

### Fallback behaviour

The application has fallback handling for supported insight and chat workflows when AI is unavailable or returns an unusable response. The exact fallback depends on the feature:

- Insight generation can use deterministic findings without AI-authored wording.
- The fitness chat can return a fixed fallback response.
- Meal-plan and grocery-list generation may return an unavailable-service response if the AI generation dependency is unavailable.

Do not assume every AI-backed feature returns the same fallback or that all AI features remain fully available without a configured API key.

### Caching and cost considerations

The insight service includes server-side caching to avoid repeatedly generating the same insight response when the relevant input findings have not changed. Chat history is bounded before being sent to the model. These measures help control repeated requests and prompt growth, but do not guarantee a particular Gemini cost or latency.

---

## Technology Stack

### Frontend

| Technology | Purpose in IFA |
|---|---|
| React 19 | Component-based user interface |
| Vite 8 | Development server and production build tooling |
| React Router DOM 7 | Client-side navigation and route configuration |
| Axios | HTTP client for backend requests |
| Framer Motion | UI animations and transitions |
| Recharts | Charts and visual analytics |
| Leaflet | Interactive map rendering |
| React Leaflet | React integration for Leaflet maps |
| MediaPipe Tasks Vision | Browser-based pose detection |
| Lucide React | Interface icons |
| React Markdown | Rendering supported Markdown content in the UI |
| ESLint | Frontend linting |

### Backend

| Technology | Purpose in IFA |
|---|---|
| Python | Backend language |
| FastAPI | REST API framework |
| Uvicorn | ASGI server |
| SQLAlchemy 2 | ORM and database access |
| Pydantic 2 | Request validation and response schemas |
| Pydantic Settings | Configuration support |
| python-jose | JWT operations |
| Passlib and bcrypt | Password hashing |
| SlowAPI | Rate limiting |
| LangChain Core | AI integration primitives |
| langchain-google-genai | Google Gemini integration |
| NumPy | Numeric operations, including correlation analysis |
| Requests / HTTPX | HTTP requests and testing client support |
| python-dotenv | Local environment-variable loading |
| email-validator | Email input validation |
| pytest | Automated backend tests |

### Data and external services

| Technology / service | Purpose |
|---|---|
| Neon PostgreSQL | Persistent relational database |
| Google Gemini | AI-assisted insights, chat, and nutrition generation |
| MediaPipe model assets | Browser-side pose landmark detection |
| OpenStreetMap | Map tiles and geographic data |
| Nominatim | Geocoding |
| Overpass API | Nearby mapped gym queries |
| Vercel | Frontend deployment |
| Render | Backend deployment |

Versions shown here reflect the repository's declared dependency ranges and package manifest at the time this README was prepared. They are not a guarantee that every hosted runtime is using the newest available version.

---

## Repository Structure

The tree below is based on the tracked files in the repository's `main` branch. **Every directory is expanded consistently**: directories are shown as directories, and tracked files inside them are listed individually. Descriptions are provided in the legend after the tree rather than replacing the contents of selected folders with summaries.

```text
AI-Gym-Fitness-Assistant/
├── .gitignore
├── LICENSE
├── README.md
├── backend/
│   ├── .env.example
│   ├── pytest.ini
│   ├── requirements.txt
│   ├── runtime.txt
│   ├── app/
│   │   ├── database.py
│   │   ├── main.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── achievement.py
│   │   │   ├── chat.py
│   │   │   ├── habit.py
│   │   │   ├── meal_plan.py
│   │   │   ├── profile.py
│   │   │   ├── user.py
│   │   │   └── workout.py
│   │   ├── routers/
│   │   │   ├── __init__.py
│   │   │   ├── achievements.py
│   │   │   ├── analytics.py
│   │   │   ├── auth.py
│   │   │   ├── consistency.py
│   │   │   ├── diet.py
│   │   │   ├── fitness_chat.py
│   │   │   ├── gym_finder.py
│   │   │   ├── habit.py
│   │   │   ├── profile.py
│   │   │   └── workout.py
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   ├── achievement.py
│   │   │   ├── analytics.py
│   │   │   ├── chat.py
│   │   │   ├── consistency.py
│   │   │   ├── context.py
│   │   │   ├── diet.py
│   │   │   ├── fitness_chat.py
│   │   │   ├── habit.py
│   │   │   ├── insight.py
│   │   │   ├── profile.py
│   │   │   ├── user.py
│   │   │   └── workout.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── achievement_service.py
│   │   │   ├── ai_insight_service.py
│   │   │   ├── analytics_service.py
│   │   │   ├── auth_service.py
│   │   │   ├── calorie_service.py
│   │   │   ├── chat_service.py
│   │   │   ├── consistency_service.py
│   │   │   ├── context_service.py
│   │   │   ├── correlation_service.py
│   │   │   ├── diet_service.py
│   │   │   ├── fitness_chat_service.py
│   │   │   ├── gemini_service.py
│   │   │   ├── gym_service.py
│   │   │   ├── habit_service.py
│   │   │   ├── profile_service.py
│   │   │   ├── progressive_overload_service.py
│   │   │   └── workout_service.py
│   └── tests/
│   │       ├── conftest.py
│   │       ├── test_ai_reliability.py
│   │       ├── test_analytics_intelligence.py
│   │       ├── test_auth_onboarding.py
│   │       ├── test_chat.py
│   │       ├── test_deletions.py
│   │       ├── test_dietician_persistence.py
│   │       └── test_progressive_overload_endpoint.py
│   └── tests/
│       ├── conftest.py
│       ├── test_ai_reliability.py
│       ├── test_analytics_intelligence.py
│       ├── test_auth_onboarding.py
│       ├── test_chat.py
│       ├── test_deletions.py
│       ├── test_dietician_persistence.py
│       └── test_progressive_overload_endpoint.py
├── frontend/
│   ├── .env.example
│   ├── .gitignore
│   ├── eslint.config.js
│   ├── index.html
│   ├── package-lock.json
│   ├── package.json
│   ├── vercel.json
│   ├── vite.config.js
│   ├── public/
│   │   ├── favicon.svg
│   │   └── icons.svg
│   └── src/
│       ├── App.jsx
│       ├── index.css
│       ├── main.jsx
│       ├── assets/
│       │   ├── hero.png
│       │   ├── react.svg
│       │   └── vite.svg
│       ├── components/
│       │   ├── ProtectedRoute.jsx
│       │   ├── charts/
│       │   │   └── WorkoutChart.jsx
│       │   ├── common/
│       │   │   ├── ConfirmDialog.jsx
│       │   │   ├── InsightList.jsx
│       │   │   ├── Navbar.jsx
│       │   │   ├── Sidebar.jsx
│       │   │   ├── StatCard.jsx
│       │   │   ├── ToastContainer.jsx
│       │   │   └── WellnessScoreWidget.jsx
│       │   ├── dashboard/
│       │   │   ├── AchievementsPanel.jsx
│       │   │   └── ConsistencyTracker.jsx
│       │   └── gymfinder/
│       │       └── GymMap.jsx
│       ├── context/
│       │   ├── AuthContext.jsx
│       │   └── ToastContext.jsx
│       ├── layouts/
│       │   └── DashboardLayout.jsx
│       ├── pages/
│       │   ├── Dashboard.jsx
│       │   ├── Dietician.jsx
│       │   ├── FitnessChat.jsx
│       │   ├── GymFinder.jsx
│       │   ├── Habits.jsx
│       │   ├── Login.jsx
│       │   ├── Profile.jsx
│       │   ├── Register.jsx
│       │   ├── Reports.jsx
│       │   ├── Webcam.jsx
│       │   └── Workout.jsx
│       ├── routes/
│       │   └── AppRoutes.jsx
│       ├── services/
│       │   ├── achievementService.js
│       │   ├── analyticsService.js
│       │   ├── api.js
│       │   ├── authService.js
│       │   ├── chatService.js
│       │   ├── consistencyService.js
│       │   ├── dietService.js
│       │   ├── gymFinderService.js
│       │   ├── habitService.js
│       │   ├── profileService.js
│       │   └── workoutService.js
│       ├── styles/
│       │   ├── auth.css
│       │   ├── confirmDialog.css
│       │   ├── dashboard.css
│       │   ├── dietician.css
│       │   ├── fitnessChat.css
│       │   ├── globals.css
│       │   ├── gymfinder.css
│       │   ├── habits.css
│       │   ├── insightList.css
│       │   ├── layout.css
│       │   ├── navbar.css
│       │   ├── profile.css
│       │   ├── reports.css
│       │   ├── responsive.css
│       │   ├── sidebar.css
│       │   ├── toast.css
│       │   ├── webcam.css
│       │   └── workout.css
│       └── utils/
│           ├── exerciseCounters.js
│           └── postAuthRedirect.js
└── screenshots/
    ├── dashboard-analytics.png
    ├── dashboard-hero.png
    ├── dietician-mealplan.png
    ├── fitness-chat.png
    ├── gym-fnder.png
    ├── habit-tracker.png
    ├── profile.png
    ├── reports-overview.png
    ├── webcam-live-detection.png
    ├── webcam-trainer.png
    └── workout-tracker.png
```

### Repository structure notes

- The tree represents tracked files returned by the GitHub `main` branch tree.
- `backend/app/models/` contains SQLAlchemy model definitions for persisted entities.
- `backend/app/routers/` contains the API route modules registered by `backend/app/main.py`.
- `backend/app/schemas/` contains request/response and context schemas.
- `backend/app/services/` contains application logic, calculations, data aggregation, external integrations, and AI orchestration.
- `backend/tests/` contains the tracked backend test suite.
- `frontend/src/pages/` contains the main routed page components.
- `frontend/src/components/` contains reusable UI components and feature-specific components.
- `frontend/src/services/` contains frontend API wrappers.
- `frontend/src/context/` contains shared React context providers.
- `frontend/src/styles/` contains the feature and layout stylesheets.
- `frontend/src/utils/` contains browser-side helpers, including exercise-counter logic.
- `screenshots/` contains the images embedded in the README.

---

## Database Model Overview

The backend uses SQLAlchemy models and a PostgreSQL database for persistent application data.

The model files in `backend/app/models/` represent the following entities:

| Model file | Entity / responsibility |
|---|---|
| `user.py` | User account and authentication-related data |
| `profile.py` | User profile and personalisation data |
| `workout.py` | Saved workout sessions |
| `habit.py` | Daily habit logs |
| `meal_plan.py` | Persisted generated nutrition plans and associated content |
| `chat.py` | Chat sessions and persisted chat messages |
| `achievement.py` | Achievement progress and unlock state |

The exact columns, constraints, relationships, and nullability should be taken from the model definitions and the deployed database schema. This overview intentionally describes the entity responsibilities rather than claiming that every production schema is identical to the current ORM model.

### Database initialization

The application entry point imports the models and calls SQLAlchemy's `Base.metadata.create_all(bind=engine)` during startup. This can create tables that do not yet exist. It is **not a schema-migration system** and does not automatically alter existing tables to match changed model definitions.

For schema changes in an existing environment, use a deliberate migration and verification process. Do not assume that restarting the backend will safely update an existing production database.

---

## API Overview

FastAPI generates the interactive API documentation at [`/docs`](https://ai-gym-fitness-assistant-e2rv.onrender.com/docs) for the deployed service. The list below summarises the router groups registered by the backend; consult the live OpenAPI schema for exact methods, paths, payloads, and response models.

| Router module | Base route / group | Responsibility |
|---|---|---|
| `auth.py` | `/auth` | Registration and login |
| `profile.py` | `/profile` | Profile retrieval, creation/update, and personalised targets |
| `workout.py` | `/workout` | Workout saving, listing, and deletion |
| `habit.py` | `/habit` | Habit-log operations |
| `diet.py` | `/diet` | Nutrition calculations, meal-plan and grocery-list workflows, and saved-plan operations |
| `analytics.py` | `/analytics` | Analytics summaries and insights |
| `consistency.py` | `/consistency` | Consistency and streak information |
| `achievements.py` | `/achievements` | Achievement status and progress |
| `fitness_chat.py` | `/fitness` | Fitness-coach chat and session history |
| `gym_finder.py` | `/gym-finder` | Location-based gym discovery |

Authentication requirements are endpoint-specific. Registration and login are public, and some general nutrition-calculation endpoints accept input without requiring a user-specific record. User-owned records and protected application features require the appropriate authentication. Check the route definitions and generated API documentation rather than assuming every endpoint has identical authentication requirements.

The webcam pose-detection loop does not have to stream frames to a backend pose endpoint. The browser processes the camera feed locally and saves the completed session through the workout API.

---

## Authentication and Security

The current codebase includes several security-related mechanisms:

- **JWT-based authentication:** The backend issues and validates bearer tokens for authenticated workflows.
- **Password hashing:** Passwords are stored as hashes using the configured Passlib/bcrypt integration rather than as plaintext.
- **Protected frontend routes:** The React router uses a protected-route component for authenticated pages.
- **Backend authentication:** Frontend route protection is not treated as a substitute for backend authorization.
- **Record ownership checks:** Supported user-owned record operations are scoped to the authenticated user.
- **Rate limiting:** SlowAPI is configured for rate limiting, with route-level limits where specified and a default limiter configured in the application.
- **CORS allow-list:** The backend configures allowed browser origins for local development and the deployed frontend.
- **Server-side AI credentials:** The Gemini API key belongs in backend environment configuration and should not be exposed through frontend variables.
- **Environment-based configuration:** Credentials and database URLs are configured outside committed source code.

### Security practices for local development and deployment

1. Never commit real database credentials, JWT secrets, or AI API keys.
2. Use a strong, unique `SECRET_KEY` in each deployed environment.
3. Keep `GEMINI_API_KEY` on the backend only.
4. Configure `VITE_API_URL` to point to the intended backend.
5. Use a separate database for development and demonstrations.
6. Do not run seed, reset, or destructive SQL scripts against production.
7. Review authentication requirements for individual endpoints in the router code and `/docs`.
8. Rotate any credential that has been accidentally exposed.

These statements describe protections present in the codebase; they are not a substitute for an independent security audit or a guarantee that a deployment is free from vulnerabilities.

---

## Getting Started

### Prerequisites

Install the following before starting local development:

- Git.
- Node.js and npm compatible with the versions supported by the frontend dependencies.
- Python compatible with the backend runtime configuration and dependencies.
- Access to a PostgreSQL database, such as a dedicated Neon development database.
- A Google Gemini API key for AI-backed features.
- A modern browser for frontend development; a camera is required to test Webcam Trainer.

Check the `engines` requirements and package compatibility for the exact versions available in your local environment. The frontend's `package-lock.json` is committed so dependency installation can use the lockfile.

### 1. Clone the repository

```bash
git clone https://github.com/dodiyariya6/AI-Gym-Fitness-Assistant.git
cd AI-Gym-Fitness-Assistant
```

### 2. Configure the backend environment

Create a Python virtual environment and install backend dependencies.

**Windows PowerShell:**

```powershell
cd backend
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

**macOS / Linux:**

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If PowerShell blocks virtual-environment activation, follow your machine's policy for running the activation script or invoke the virtual environment's Python executable directly.

### 3. Create the backend environment file

Copy `backend/.env.example` to `backend/.env`, then replace all placeholder values with valid development credentials.

Do not paste real secrets into source files or commit the `.env` file.

See [Environment Variables](#environment-variables) for the variables expected by the application.

### 4. Prepare a development database

Use a **dedicated development database**. Do not point local experiments or test seed scripts at the production database.

Set `DATABASE_URL` in `backend/.env` to the PostgreSQL connection string for that development database. Confirm that the database accepts connections from your development environment.

On startup, the application calls `Base.metadata.create_all()` for tables represented by the imported SQLAlchemy models. This creates missing tables but does not migrate existing table definitions. If the database has an older schema, reconcile it deliberately before using the application.

### 5. Install frontend dependencies

Open a second terminal at the repository root:

```bash
cd frontend
npm ci
```

`npm ci` installs the versions captured in `package-lock.json`. Use `npm install` only when you intentionally need to update the lockfile.

### 6. Configure the frontend environment

Copy `frontend/.env.example` to `frontend/.env` and set `VITE_API_URL` to the local backend URL:

```env
VITE_API_URL=http://127.0.0.1:8000
```

Vite exposes variables prefixed with `VITE_` to client-side code. **Never put a secret or private database credential in a `VITE_` variable.**

---

## Environment Variables

### Backend — `backend/.env`

| Variable | Required | Purpose |
|---|---|---|
| `DATABASE_URL` | Yes | SQLAlchemy database connection string |
| `GEMINI_API_KEY` | Required for Gemini-backed generation | Google Gemini API credential |
| `SECRET_KEY` | Yes | Secret used for signing/verifying JWTs |
| `ALGORITHM` | Yes / configured | JWT algorithm; the example uses `HS256` |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Yes / configured | Token lifetime in minutes |

Example format only:

```env
DATABASE_URL=postgresql://user:password@host/database?sslmode=require
GEMINI_API_KEY=replace_with_your_real_key
SECRET_KEY=replace_with_a_long_random_secret
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

Replace the placeholders before starting the backend. Do not use the example database URL or secret as real credentials.

### Frontend — `frontend/.env`

| Variable | Example | Purpose |
|---|---|---|
| `VITE_API_URL` | `http://127.0.0.1:8000` | Base URL of the backend API |

Local frontend environment:

```env
VITE_API_URL=http://127.0.0.1:8000
```

For the deployed frontend, the value should point to the intended deployed backend. After changing a Vite environment variable, restart the development server or rebuild/redeploy the frontend as appropriate.

---

## Running the Application

Run the backend and frontend in separate terminals.

### Terminal 1 — Backend

From the repository root:

```bash
cd backend
uvicorn app.main:app --reload
```

By default, the backend is available at:

- API root: `http://127.0.0.1:8000/`
- Interactive API documentation: `http://127.0.0.1:8000/docs`
- OpenAPI schema: `http://127.0.0.1:8000/openapi.json`

If your environment uses a different host or port, update the frontend's `VITE_API_URL` to match.

### Terminal 2 — Frontend

From the repository root:

```bash
cd frontend
npm run dev
```

Vite prints the local development URL in the terminal. The usual default is `http://localhost:5173`.

### Production frontend build

To create a production build and serve it locally for preview:

```bash
cd frontend
npm run build
npm run preview
```

The production output is generated by Vite. `npm run preview` is intended for local preview, not as a replacement for the configured production hosting platform.

### Frontend lint

```bash
cd frontend
npm run lint
```

The lint command runs ESLint against the frontend code. Resolve reported issues before treating the lint step as passed.

---

## Testing

The backend uses `pytest`. The tracked test suite includes tests for selected authentication, analytics, AI-reliability, chat, deletion, Dietician persistence, and progressive-overload behaviour.

### Run the backend test suite

From the repository root:

```bash
cd backend
pytest
```

The repository includes `backend/pytest.ini` and a shared test fixture file. The tests are designed to isolate selected behaviours and avoid relying on a live production database or making uncontrolled real AI calls.

### Test areas represented in the repository

| Test file | Main area |
|---|---|
| `test_auth_onboarding.py` | Authentication and onboarding behaviour |
| `test_analytics_intelligence.py` | Analytics and insight-related behaviour |
| `test_ai_reliability.py` | Supported AI-unavailable/fallback behaviour |
| `test_chat.py` | Chat session and history behaviour |
| `test_deletions.py` | Deletion and ownership-related behaviour |
| `test_dietician_persistence.py` | Persisted nutrition-plan workflows |
| `test_progressive_overload_endpoint.py` | Progressive-overload endpoint behaviour |

These filenames describe the main focus of each test module, not an exhaustive list of assertions within it.

### Frontend verification

The package manifest defines these scripts:

```bash
npm run dev
npm run build
npm run lint
npm run preview
```

The existence of these scripts does not mean that an automated frontend end-to-end test suite is included. Before a release or demonstration, manually verify registration/login, profile completion, workout and habit logging, nutrition generation/history, chat, reports, Gym Finder, and camera permissions in the target browser.

### Interpreting test results

A passing test suite means the included tests passed in the environment in which they were run. It does not prove complete code coverage, successful production end-to-end operation, or availability of external providers such as Gemini, Neon, Nominatim, or Overpass.

---

## Deployment

The repository is configured around a separate frontend and backend deployment.

| Component | Platform | Configured resource |
|---|---|---|
| Frontend | Vercel | [Web application](https://ai-gym-fitness-assistant-beta.vercel.app) |
| Backend | Render | [Backend API](https://ai-gym-fitness-assistant-e2rv.onrender.com) |
| API documentation | Render / FastAPI | [Swagger UI](https://ai-gym-fitness-assistant-e2rv.onrender.com/docs) |
| Database | Neon | PostgreSQL connection configured through `DATABASE_URL` |
| AI provider | Google Gemini | Configured through backend `GEMINI_API_KEY` |

### Frontend deployment checklist

1. Set `VITE_API_URL` to the correct backend URL in the frontend hosting environment.
2. Confirm that the configured backend CORS allow-list includes the deployed frontend origin.
3. Build the frontend with the configured production environment variables.
4. Verify authentication, API calls, and page navigation after deployment.
5. Test camera access over HTTPS in a supported browser.
6. Verify that the browser can load MediaPipe model and WASM assets.

### Backend deployment checklist

1. Install dependencies from `backend/requirements.txt`.
2. Configure `DATABASE_URL`, `SECRET_KEY`, `ALGORITHM`, and `ACCESS_TOKEN_EXPIRE_MINUTES`.
3. Configure `GEMINI_API_KEY` if AI-backed features are required.
4. Confirm that the database schema is compatible with the application models.
5. Configure allowed CORS origins for the intended frontend.
6. Inspect backend logs and the `/docs` endpoint after deployment.
7. Test authenticated endpoints using a newly issued token.

### Database safety

Use separate database credentials and databases for development, testing, demo data, and production where appropriate. Do not create demo records by running destructive SQL against the production database. A database branch or clone can contain copied production records; it should not be assumed to be an empty or privacy-safe demo environment.

---

## Known Limitations

- **AI provider availability:** AI-authored insights, chat replies, meal plans, and grocery lists depend on the relevant Gemini workflows. Fallback behaviour differs by feature.
- **AI-generated nutrition:** Meal plans and grocery lists are generated content and may need human review for allergies, medical conditions, dietary restrictions, or nutritional suitability.
- **Estimated calories:** Workout calories are calculated estimates based on available session and body-weight inputs, not direct physiological measurements.
- **Pose estimation:** Camera angle, lighting, occlusion, device performance, and movement execution can affect pose landmarks, repetition counts, and form scores.
- **Wellness score interpretation:** The score is an application-defined metric. It is not a clinical measure of health.
- **Workout-completion component:** The current wellness breakdown's `workout_completion` rate is based on distinct days with habit logs in the rolling seven-day period, not a verified count of workout sessions.
- **Correlation interpretation:** Habit/workout correlation indicates association and does not establish causation.
- **Gym data quality:** Gym Finder depends on mapped geographic data and public external services. Coverage and availability vary by area and service status.
- **Schema evolution:** `Base.metadata.create_all()` does not migrate existing database tables. Existing environments need deliberate schema migration and verification when models change.
- **Concurrency:** The habit service's application-level duplicate check is not, by itself, a database-enforced guarantee against simultaneous duplicate submissions.
- **Historical data requirements:** Trends and progressive-overload classifications are less informative when an account has few or inconsistent records.
- **Automated test scope:** The tracked automated suite focuses on selected backend behaviours; it should not be represented as complete frontend end-to-end coverage.
- **Hosting dependencies:** The public application depends on external hosting, database, AI, model-CDN, and map-service availability.

---

## Future Improvements

Potential improvements that build on the current architecture include:

- Expand automated frontend and browser end-to-end coverage.
- Add more comprehensive schema migrations and migration checks.
- Add database-enforced constraints for invariants such as one habit log per user per date, together with conflict handling.
- Add pagination and filtering for longer workout, habit, and chat histories.
- Improve observability for AI provider errors, latency, rate limits, and external map-service failures.
- Add clearer user-facing indicators when content is generated by AI versus produced by deterministic fallback logic.
- Improve the accessibility and explanatory detail of wellness and workout analytics.
- Add stronger validation and user controls for nutrition preferences, allergies, and excluded ingredients.
- Expand exercise coverage and test pose-counter behaviour across camera angles and device classes.
- Review deployment scaling, backup, and operational monitoring requirements as usage grows.

These are suggested improvements, not claims that the features are already implemented.

---

## Contributing

Contributions and issue reports should be focused and reproducible.

1. Fork the repository or create a feature branch.
2. Keep changes scoped to the relevant frontend or backend module.
3. Do not commit environment files, secrets, or personal data.
4. Run the relevant backend tests and frontend lint/build checks.
5. Document new environment variables, API changes, and setup requirements.
6. Update this README when tracked paths, setup steps, screenshots, or externally visible behaviour change.
7. Include reproduction steps and expected versus actual behaviour when reporting a bug.

For changes to authentication, database models, migrations, or user-owned records, verify both successful access and cross-user isolation.

---

## License

This project is distributed under the [MIT License](LICENSE).

---

## Author

**Riya Dodiya**

IFA was developed as an academic engineering project covering full-stack web development, API design, relational database integration, AI service integration, browser-based computer vision, analytics, testing, and deployment.
