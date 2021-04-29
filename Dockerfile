FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /app

COPY pyproject.toml ./
#COPY poetry.lock ./

RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

ENV PYTHONPATH app

# CMD uvicorn src.main:app --reload --workers 1 --host 0.0.0.0
