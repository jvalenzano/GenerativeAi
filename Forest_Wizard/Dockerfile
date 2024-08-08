FROM python:3.9.1-alpine
WORKDIR /app
ADD . /app
COPY . .
RUN pip install --upgrade pip
COPY ./Forest_Wizard/requirements.txt .
RUN pip install  -r requirements.txt
EXPOSE 80
CMD ["python","app.py"]
