from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
import os

# Database path can be overridden with the DB_PATH environment variable
DB_PATH = os.environ.get("DB_PATH") or os.path.join(os.path.dirname(__file__), "items.db")


class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    conn.execute(
        """
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        price REAL NOT NULL
    )
    """
    )
    conn.commit()
    conn.close()


app = FastAPI(title="Persistent CRUD API")


@app.on_event("startup")
def on_startup():
    init_db()


@app.post("/items/", response_model=Item, status_code=201)
def create_item(item: Item):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO items (name, description, price) VALUES (?, ?, ?)",
        (item.name, item.description, item.price),
    )
    conn.commit()
    item_id = cur.lastrowid
    conn.close()
    return {**item.dict(), "id": item_id}


@app.get("/items/", response_model=List[Item])
def list_items():
    conn = get_connection()
    cursor = conn.execute("SELECT id, name, description, price FROM items")
    rows = cursor.fetchall()
    conn.close()
    items = [
        Item(id=row["id"], name=row["name"], description=row["description"], price=row["price"])
        for row in rows
    ]
    return items


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    conn = get_connection()
    cursor = conn.execute("SELECT id, name, description, price FROM items WHERE id = ?", (item_id,))
    row = cursor.fetchone()
    conn.close()
    if row is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return Item(id=row["id"], name=row["name"], description=row["description"], price=row["price"])


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE items SET name = ?, description = ?, price = ? WHERE id = ?",
        (item.name, item.description, item.price, item_id),
    )
    if cur.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Item not found")
    conn.commit()
    conn.close()
    return {**item.dict(), "id": item_id}


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM items WHERE id = ?", (item_id,))
    if cur.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Item not found")
    conn.commit()
    conn.close()
    return None


def run():
    import uvicorn

    init_db()
    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    run()
