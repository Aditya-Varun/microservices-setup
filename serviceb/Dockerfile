FROM python:3.8-slim

WORKDIR /app
COPY . /app
# Copy the requirements file
COPY requirements.txt /app/
RUN pip install -r requirements.txt

EXPOSE 8002
CMD ["python", "app.py"]
