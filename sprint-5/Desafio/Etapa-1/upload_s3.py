import boto3
from dotenv import load_dotenv
import datetime
import os

load_dotenv()

bucket = os.getenv('AWS_BUCKET_NAME')
hoje = datetime.datetime.now().strftime('%Y-%m-%d')

ARQUIVO_CSV_FILMES = '/app/assets/movies.csv'
ARQUIVO_CSV_SERIES = '/app/assets/series.csv'
DESTINO_S3 = f'Raw/Local/CSV/{hoje[0:4]}/{hoje[5:7]}/{hoje[8:10]}/'

print(DESTINO_S3)

s3 = boto3.client('s3')

try:
    s3.upload_file(ARQUIVO_CSV_FILMES, bucket, DESTINO_S3 + 'movies.csv')
    s3.upload_file(ARQUIVO_CSV_SERIES, bucket, DESTINO_S3 + 'series.csv')
    print("Subiu o arquivo!")
except Exception as e:
    print(f"Erro ao subir o arquivo: {e}")