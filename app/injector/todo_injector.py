from dependency_injector import containers, providers
from dependency_injector.wiring import inject, Provide
from usecase.todo.todo_get_usecase import TodoGetUsecase


class Container(containers.DeclarativeContainer):
    todo_get = providers.Factory(TodoGetUsecase)
