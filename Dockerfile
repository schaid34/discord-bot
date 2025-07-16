FROM python:3.11-slim

# Install dependencies (ffmpeg + others)
RUN apt update && \
    apt install -y ffmpeg libffi-dev libnacl-dev

# Set working directory
WORKDIR /app

# Copy code
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the bot
CMD ["python", "main.py"]
