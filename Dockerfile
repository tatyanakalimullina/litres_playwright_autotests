FROM mcr.microsoft.com/playwright/python:v1.64.1

WORKDIR /app

# uv внутрь образа
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# сначала только зависимости — этот слой кэшируется, пока lock-файл не меняется
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen

# затем код (см. .dockerignore — мусор и локальный .venv в образ не попадают)
COPY . .

CMD [".venv/bin/pytest", "--alluredir=allure-results"]
