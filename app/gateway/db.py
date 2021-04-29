import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


db_host = os.getenv("DB_HOST", "db")
db_name = os.getenv("DB_NAME", "db_name")
db_user = os.getenv("DB_USER", "root")
db_password = os.getenv("DB_PASSWORD", "root")
db_url = f"mysql://{db_user}:{db_password}@{db_host}:3306/{db_name}"

engine = create_engine(db_url, encoding="utf-8", echo=False)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = Session()

Base = declarative_base()
