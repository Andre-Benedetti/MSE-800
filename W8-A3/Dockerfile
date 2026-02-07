# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Create an environment variable for the API Key
# (We will override this at runtime for security)
ENV GEMINI_API_KEY="your_api_key_here"

# Run the application
CMD ["python", "app.py"]