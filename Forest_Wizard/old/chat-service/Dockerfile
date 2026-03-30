FROM python:3.14.0rc1-alpine
RUN addgroup -S nonroot && adduser -S nonroot -G nonroot
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
USER nonroot
CMD ["python","app.py"]
