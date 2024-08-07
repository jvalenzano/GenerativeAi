FROM python:3.9.1-alpine
RUN pip install --upgrade pip
WORKDIR /application
ADD . /application/
 

EXPOSE 8080
CMD ["python","app.py"]
