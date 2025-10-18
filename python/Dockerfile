FROM python:3.11.2

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy semua file project
COPY . .

# Expose port untuk FastAPI
EXPOSE 8000

# Jalankan aplikasi dengan uvicorn (lebih cocok untuk FastAPI)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
