FROM python:3.14.0-alpine
RUN addgroup -S nonroot && adduser -S nonroot -G nonroot
WORKDIR /Forest_Wizard
COPY ./Forest_Wizard/requirements.txt .
COPY ./Forest_Wizard/app.py .
COPY ./Forest_Wizard/templates ./templates
COPY ./Forest_Wizard/static ./static
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN chown -R nonroot:nonroot /Forest_Wizard
RUN chmod +x /Forest_Wizard/app.py
USER nonroot
EXPOSE 80
CMD ["python", "app.py"]
