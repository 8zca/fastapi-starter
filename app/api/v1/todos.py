from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide
from app.injector.todo_injector import Container
from app.usecase.todo.todo_get_usecase import TodoGetInput
import sys

router = APIRouter()


@router.get("/")
@inject
def read_items(usecase=Depends(Provide[Container.todo_get])):
    todos = usecase.call(input=TodoGetInput())
    return {"todos": todos}


@router.get("/{id}")
def read_item(id: int):
    return {"id": id}


container = Container()
container.wire(modules=[sys.modules[__name__]])
