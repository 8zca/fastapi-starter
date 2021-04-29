from fastapi import APIRouter
from app.domain.model.todo.todo_repository import TodoRepository
from app.gateway import db
from app.domain.model.todo.todo import Todo

router = APIRouter()


@router.get("/")
def read_items():
    repo = TodoRepository()
    todos = repo.all()

    return {"todos": todos}


@router.get("/{id}")
def read_item(id: int):
    return {"id": id}
