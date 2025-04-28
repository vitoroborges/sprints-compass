FROM python:3.9-slim
RUN pip install boto3 python-dotenv
WORKDIR /app
COPY upload_s3.py .
COPY .env .
COPY /assets assets/
CMD ["python", "upload_s3.py"]