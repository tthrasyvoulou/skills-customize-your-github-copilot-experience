# 📘 Assignment: Persistent CRUD API with SQLite

## 🎯 Objective

Build a small RESTful API using FastAPI that persists data to a local SQLite database. Students will implement full CRUD operations, input validation with Pydantic models, and provide clear run instructions.

## 📝 Tasks

### 🛠️ Core: Persistent CRUD API

#### Description
Create an API to manage a collection of items. Implement endpoints to create, read, update and delete items. Store items persistently in a SQLite database so data survives server restarts.

#### Requirements
Completed program should:

- Provide the following endpoints:
  - `GET /items/` — list all items
  - `GET /items/{id}` — retrieve a single item by ID
  - `POST /items/` — create a new item
  - `PUT /items/{id}` — update an existing item
  - `DELETE /items/{id}` — delete an item
- Use `pydantic.BaseModel` for request and response models.
- Return appropriate HTTP status codes (`201` for create, `204` for delete, `404` when not found).
- Persist items to a local SQLite database (use the built-in `sqlite3` module).
- Provide example requests and clear run instructions.

### 🛠️ Extra Credit

#### Description
Add automated tests using `pytest` that cover at least two endpoints, or add simple filtering/query parameters to the list endpoint.

## ✅ Deliverables

- `starter-code.py` with your implementation or improvements
- This `README.md` describing how to run and test the API
- (Optional) `requirements.txt`, tests, or migration scripts

## ⚙️ Setup & Run

### Prerequisites

- Python 3.9+ (3.10+ recommended)
- `pip` and a virtual environment

### Install and run

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python assignments/fastapi-persistent-crud/starter-code.py
```

Open http://127.0.0.1:8000/docs for the interactive API docs (Swagger UI).

## 🔎 Example requests

Create an item:

```bash
curl -sS -X POST http://127.0.0.1:8000/items/ \
  -H "Content-Type: application/json" \
  -d '{"name":"Notebook","description":"200 pages","price":4.5}'
```

List items:

```bash
curl -sS http://127.0.0.1:8000/items/
```

Get an item:

```bash
curl -sS http://127.0.0.1:8000/items/1
```

Update an item:

```bash
curl -sS -X PUT http://127.0.0.1:8000/items/1 \
  -H "Content-Type: application/json" \
  -d '{"name":"Notebook XL","description":"300 pages","price":6.0}'
```

Delete an item:

```bash
curl -sS -X DELETE http://127.0.0.1:8000/items/1
```

## 💡 Hints

- Initialize the database on startup and create the `items` table if it does not exist.
- Keep database access in simple helper functions to keep routes focused on request/response handling.
- Use `pydantic` models to validate input and shape responses.
