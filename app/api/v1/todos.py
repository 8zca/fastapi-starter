from fastapi import APIRouter, Depends
from app.domain.model.todo.todo_repository import TodoRepository
from dependency_injector.wiring import inject, Provide
from injector.todo_injector import Container
from usecase.todo.todo_get_usecase import TodoGetInput
from dependency_injector import containers, providers
from dependency_injector.wiring import inject, Provide
import sys


router = APIRouter()


@router.get("/")
@inject
def read_items(usecase = Depends(Provide[Container.todo_get])):
    todos = usecase.call(input=TodoGetInput())
    return {"todos": todos}


@router.get("/{id}")
def read_item(id: int):
    return {"id": id}


container = Container()
container.wire(modules=[sys.modules[__name__]])
