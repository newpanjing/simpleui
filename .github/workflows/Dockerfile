# Use official Python image with correct version
FROM python:3.11.8-slim

# Install system dependencies: PostgreSQL client and Redis
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
         gcc \
         libpq-dev \
         redis-server \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app/api/tacticalrmm

# Copy requirements files first (for efficient build caching)
COPY api/tacticalrmm/requirements*.txt ./
COPY api/tacticalrmm/settings.py ./

# Extract/set setuptools and wheel versions dynamically (optional: set defaults here if needed)
ARG SETUPTOOLS_VER=latest
ARG WHEEL_VER=latest

# Install pip, setuptools, wheel (use values from settings.py if automated, or set fixed versions below)
RUN pip install --upgrade pip==25.1 \
  && pip install setuptools==$SETUPTOOLS_VER wheel==$WHEEL_VER \
  && pip install -r requirements.txt -r requirements-test.txt

# Copy rest of the source code
COPY . /app

# Start Redis server in background (for local/dev use)
RUN service redis-server start

# Expose port if running server
EXPOSE 8000

# Default CMD (customize for your app)
CMD ["pytest"]
# Or, if you want to run Django by default: ["python", "manage.py", "runserver", "0.0.0.0:8000"]
