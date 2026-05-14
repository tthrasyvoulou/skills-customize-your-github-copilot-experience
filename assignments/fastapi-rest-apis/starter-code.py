from typing import Optional, List, Dict
from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel, Field
import uuid


class Task(BaseModel):
    id: Optional[str] = None
    title: str = Field(..., example="Buy milk")
    description: Optional[str] = Field(None, example="2 liters of milk")
    done: bool = False


app = FastAPI(title="To-Do API (Starter)")

# Simple in-memory store: {id: task_dict}
TASKS: Dict[str, dict] = {}


@app.get("/tasks", response_model=List[Task])
def list_tasks():
    return list(TASKS.values())


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: str):
    task = TASKS.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task: Task):
    task_id = str(uuid.uuid4())
    task.id = task_id
    TASKS[task_id] = task.dict()
    return TASKS[task_id]


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: str, task_update: Task):
    existing = TASKS.get(task_id)
    if existing is None:
        raise HTTPException(status_code=404, detail="Task not found")
    task_update.id = task_id
    TASKS[task_id] = task_update.dict()
    return TASKS[task_id]


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: str):
    if task_id not in TASKS:
        raise HTTPException(status_code=404, detail="Task not found")
    del TASKS[task_id]
    return Response(status_code=204)


def run():
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    run()
