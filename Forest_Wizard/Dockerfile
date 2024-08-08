FROM python:3.9.1-alpine
WORKDIR /app
COPY . .
COPY ../Forest_Wizard/requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python","app.py"]
