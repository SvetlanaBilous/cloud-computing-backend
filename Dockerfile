# Use Python 3.12
FROM python:3.12-slim

# Work directory
WORKDIR /app

# Copy dependenses and installing it
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Port open
EXPOSE 8080

# Run app
CMD ["python", "app.py"]