from app.gateway import db
from app.domain.model.todo.todo import Todo


class TodoRepository:
    def all(self):
        try:
            todos = db.session.query(Todo).all()
        except SQLAlchemyError:
            raise

        return todos
