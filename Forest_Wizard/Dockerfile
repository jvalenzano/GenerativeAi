FROM python:3.9.1-alpine
RUN pip install --upgrade pip
COPY ./Forest_Wizard/requirements.txt .
COPY ./Forest_Wizard/app.py .
COPY ./Forest_Wizard/templates/index.html .
COPY ./Forest_Wizard/static .
RUN pip install  -r requirements.txt
EXPOSE 80
CMD ["python","app.py"]
