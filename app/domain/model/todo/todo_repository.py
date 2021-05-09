from app.gateway import db
from app.domain.model.todo.todo import Todo
from sqlalchemy.exc import SQLAlchemyError


class TodoRepository:
    def all(self):
        try:
            todos = db.session.query(Todo).all()
        except SQLAlchemyError:
            raise

        return todos
