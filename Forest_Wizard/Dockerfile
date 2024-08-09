FROM python:3.9.1-alpine
WORKDIR /Forest_Wizard
COPY ./Forest_Wizard/requirements.txt .
COPY ./Forest_Wizard/app.py .
COPY ./Forest_Wizard/templates ./templates
COPY ./Forest_Wizard/static ./static
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 80
CMD ["python", "app.py"]
