FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy and install dependencies first (for caching)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Add a non-root user *after* copying files and installing packages
RUN useradd -m appuser && chown -R appuser /app
USER appuser

# Healthcheck
HEALTHCHECK CMD curl --fail http://localhost:5000/ || exit 1

# Run the app
CMD ["python", "app.py"]
