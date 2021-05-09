from dependency_injector import containers, providers
from app.usecase.todo.todo_get_usecase import TodoGetUsecase


class Container(containers.DeclarativeContainer):
    todo_get = providers.Factory(TodoGetUsecase)
