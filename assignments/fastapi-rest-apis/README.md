# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small RESTful API using the FastAPI framework and Pydantic models. You will implement routing, request/response validation, and basic CRUD operations.

## 📝 Tasks

### 🛠️ To-Do API (Core)

#### Description
Create a simple To-Do REST API to manage tasks. Implement endpoints for creating, reading, updating, and deleting tasks. Use Pydantic models for input validation and return appropriate HTTP status codes.

#### Requirements
Completed program should:

- Provide the following endpoints:
  - `GET /tasks` — list all tasks
  - `GET /tasks/{id}` — retrieve a single task by ID
  - `POST /tasks` — create a new task
  - `PUT /tasks/{id}` — update an existing task
  - `DELETE /tasks/{id}` — remove a task
- Use `pydantic.BaseModel` for request and response models.
- Return appropriate HTTP status codes (`201` for create, `204` for delete, `404` when not found).
- Store tasks in an in-memory dictionary for this assignment (persistence is optional extra credit).
- Include example requests and clear run instructions.

### 🛠️ Extra Credit: Persistence or Authentication

#### Description
Extend the API to add persistence or basic authentication.

#### Requirements

- Persist tasks using SQLite (via `sqlite3` or `SQLAlchemy`) and update the API accordingly, or
- Add token-based authentication (JWT or similar) so that only authenticated clients can create/update/delete tasks, or
- Add automated tests (`pytest`) covering at least two endpoints.

## ✅ Deliverables

- `starter-code.py` with your implementation or improvements
- This `README.md` describing how to run and test the API
- (Optional) Tests, migration files, or other extras

## ⚙️ Setup & Run

### Prerequisites

- Python 3.9+ (3.10+ recommended)
- `pip` and a virtual environment

### Install and run

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python assignments/fastapi-rest-apis/starter-code.py
```

Open http://127.0.0.1:8000/docs for the interactive API docs (Swagger UI).

## 🔎 Example requests

Create a task:

```bash
curl -sS -X POST http://127.0.0.1:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Buy milk","description":"2 liters"}'
```

List tasks:

```bash
curl -sS http://127.0.0.1:8000/tasks
```

Get a task:

```bash
curl -sS http://127.0.0.1:8000/tasks/<task_id>
```

Update a task:

```bash
curl -sS -X PUT http://127.0.0.1:8000/tasks/<task_id> \
  -H "Content-Type: application/json" \
  -d '{"title":"Buy almond milk","done":true}'
```

Delete a task:

```bash
curl -sS -X DELETE http://127.0.0.1:8000/tasks/<task_id>
```

## 💡 Hints

- Use Pydantic models to validate input and shape responses.
- Keep the starter implementation simple (in-memory store). Focus on clear API contracts.
- Use `uvicorn` for local development when you want auto-reload or different host/port settings.
