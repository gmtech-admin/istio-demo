FROM python:3.11-slim

WORKDIR /app

# Install build backend
RUN pip install --no-cache-dir hatchling

# Copy project metadata first (better caching)
COPY pyproject.toml .

# Install dependencies (no source code yet)
RUN pip install --no-cache-dir .

# Copy source code
COPY src/ src/

EXPOSE 8080

CMD ["python", "src/hostname_app/app.py"]
