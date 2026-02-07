FROM python:3.11-slim

WORKDIR /app

# Explicitly copy the requirements first to force a new layer
COPY requirements.txt .

# Install dependencies and print them to the console so we can see
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the files
COPY . .

CMD ["python", "app.py"]