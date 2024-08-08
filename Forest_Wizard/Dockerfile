FROM python:3.9.1-alpine
WORKDIR /Forest_Wizard
COPY . .
RUN pip install --upgrade pip
COPY ./Forest_Wizard/requirements.txt .
RUN pip install  -r requirements.txt
EXPOSE 8080
CMD ["python","app.py"]
