FROM python:3.13.3-alpine
RUN addgroup -S nonroot && adduser -S nonroot -G nonroot
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
USER nonroot
CMD ["python","app.py"]
