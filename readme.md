# Answerly Backend

Answerly is a **backend-first, community-driven Question & Answer (Q&A) platform**.  
This repository contains the **backend only**, built using **Django** and **Django REST Framework**, with a fully decoupled architecture designed to support any frontend (web or mobile).

The project focuses on **clean API design, authentication, permissions, and real business logic**, rather than just basic CRUD operations.

---

## Features

- JWT Authentication (login & refresh)
- Questions & Answers APIs
- Answer filtering by question
- Generic voting system (questions & answers)
- Vote counts (upvotes / downvotes)
- Author-only edit & delete permissions
- User reputation system (automatic, via Django signals)
- User profile API (reputation)
- Tag system for questions
- Question filtering by tag
- Public user profiles (view by username)
- Backend-first, frontend-agnostic design

---

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite (local development)
- PostgreSQL (production-ready)
- Simple JWT (authentication)

---

## Project Structure

```
answerly-backend/
├── answerly/ # Django project configuration
├── apps/
│ ├── accounts # Authentication, profile, reputation
│ ├── questions # Questions logic
│ ├── answers # Answers logic
│ ├── votes # Voting system
│ └── tags # Tags (extensible)
├── Answerly.postman_collection.json
├── requirements.txt
├── manage.py
└── README.md
```


---

## Authentication (JWT)

Authentication is handled using **JWT (SimpleJWT)**.

### Login
`POST /api/auth/login/`


Returns:
- `access` token (short-lived)
- `refresh` token (long-lived)

### Refresh Access Token
`POST /api/auth/refresh/`


Use the refresh token to obtain a new access token.

All protected endpoints require:

`Authorization: Bearer <access_token>`


---

## Reputation System

Reputation is automatically updated using **Django signals**.

### Rules
- Upvote on your content → **+10 reputation**
- Downvote on your content → **-2 reputation**
- Self-voting is not allowed

Reputation is stored in a **Profile model** linked one-to-one with the User.

---

## Permissions

- Anyone can **read** questions and answers
- Only authenticated users can **create** content
- Only the **author** can update or delete their question or answer
- Voting is restricted to authenticated users

---

## API Overview

### Questions
- `GET /api/questions/` – List questions
- `GET /api/questions/?tag=<tag>` – Filter questions by tag
- `POST /api/questions/` – Create question
- `PATCH /api/questions/{id}/` – Update (author only)
- `DELETE /api/questions/{id}/` – Delete (author only)


### Answers
- `GET /api/answers/?question=<id>` – List answers for a question
- `POST /api/answers/` – Create answer
- `PATCH /api/answers/{id}/` – Update answer (author only)
- `DELETE /api/answers/{id}/` – Delete answer (author only)


### Voting
- `POST /api/vote/` – Vote on a question or answer

### Profile
- `GET /api/profile/` – Get logged-in user profile
- `GET /api/profile/<username>/` – Public user profile


---

## API Testing (Postman)

APIs were tested using **Postman**.

The Postman collection is included in the repository:

`Answerly.postman_collection.json`


### Postman Environment Setup
Create a Postman environment with:
- `base_url = http://127.0.0.1:8000`
- `access` (auto-set on login)
- `refresh` (auto-set on login)

---

## Local Setup

1. Clone the repository
2. Create a virtual environment
3. Install dependencies
   
   `pip install -r requirements.txt`

4. Run migrations

    `python manage.py migrate`


5. Start the server

    `python manage.py runserver`

---

## Project Focus

This project was built to:
- Practice real-world backend architecture
- Understand authentication & authorization deeply
- Implement business logic using Django signals
- Build clean, reusable APIs
---


## Author

**Akshay Gite**

---