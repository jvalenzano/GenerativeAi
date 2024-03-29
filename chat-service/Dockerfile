FROM python:3.9.1-alpine
RUN pip install --upgrade pip
WORKDIR /application
ADD . /application/
RUN pip install -r requirements.txt 
CMD ["python","app.py"]
