# syntax=docker/dockerfile:1

FROM python:3.12-slim AS base
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
COPY tests ./tests

# Dev/test stage
FROM base AS test
WORKDIR /app
ENV PYTHONPATH=/app
CMD ["pytest", "-q"]

# Runtime stage
FROM base AS runtime
EXPOSE 5000
CMD ["python", "-m", "app.app"]
