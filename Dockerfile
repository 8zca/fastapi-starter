FROM tiangolo/uvicorn-gunicorn:python3.8-slim

WORKDIR /app

COPY pyproject.toml ./
COPY poetry.lock ./

RUN apt-get update -qq \
    && apt-get dist-upgrade -yq \
    && apt-get install -yq --no-install-recommends \
      build-essential \
      default-libmysqlclient-dev \
      default-mysql-client \
    && pip install --upgrade pip \
    && pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && truncate -s 0 /var/log/*log \
    && rm -rf ~/.cache/pypoetry/{cache,artifacts}

ENV PYTHONPATH app

# CMD uvicorn src.main:app --reload --workers 1 --host 0.0.0.0
