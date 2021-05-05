from typing import Union, List, Optional
from usecase.base import BaseHandler
from app.domain.model.todo.todo_repository import TodoRepository
from pydantic import BaseModel, Field


class TodoGetInput(BaseModel):
    id: Optional[int] = None



class TodoGetOutput(BaseModel):
    id: int = Field(...)
    todo: str = Field(...)
    status: str = Field(...)


class TodoGetUsecase(BaseHandler):
    def call(self, input: TodoGetInput) -> Optional[Union[TodoGetOutput, List[TodoGetOutput]]]:
        repository = TodoRepository()

        if input.id:
            # find by id
            return TodoGetOutput(id=1, todo='test', status='doing')
        else:
            # get all
            data = repository.all()

            response = []
            for d in data:
                response.append(TodoGetOutput(id=d.id, todo=d.todo, status=d.status))
            return response
