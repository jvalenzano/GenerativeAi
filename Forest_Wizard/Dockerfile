FROM python:3.9.1-alpine
RUN pip install --upgrade pip
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python","app.py"]
