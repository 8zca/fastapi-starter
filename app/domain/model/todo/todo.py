from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.gateway.db import Base


class Todo(Base):
    """
    Todo
    """

    __tablename__ = "todos"

    id = Column("id", Integer(), primary_key=True, autoincrement=True)
    todo = Column("todo", String(255), nullable=False)
    status = Column("status", String(12), nullable=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)    

    def __init__(
        self,
        todo: str,
        status: str,
        created_at: datetime,
        updated_at: datetime
    ):
        self.todo = todo
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at
