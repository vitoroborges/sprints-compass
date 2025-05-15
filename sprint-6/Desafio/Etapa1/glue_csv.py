import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import col, current_date, year, month, dayofmonth, concat_ws
from pyspark.sql.types import IntegerType, FloatType


# Argumentos esperados
args = getResolvedOptions(sys.argv, [
    'JOB_NAME',
    'S3_LOCAL_TARGET_PATH',
    'S3_CSV_SOURCE',
    'S3_TMDB_SOURCE',
    'S3_TMDB_TARGET_PATH'
])

local_target_path = args['S3_LOCAL_TARGET_PATH']
tmdb_target_path = args['S3_TMDB_TARGET_PATH']
csv_source = args['S3_CSV_SOURCE']
tmdb_source = args['S3_TMDB_SOURCE']

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
                      
csv_df = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [csv_source]},
    format="csv"
).toDF()

for nome_coluna in csv_df.columns:
    csv_df = csv_df.withColumnRenamed(nome_coluna, nome_coluna.strip())

csv_df = csv_df.dropDuplicates()

csv_df = csv_df.withColumn("data_ingestao", current_date()) \
       .withColumn("ano", year("data_ingestao")) \
       .withColumn("mes", month("data_ingestao")) \
       .withColumn("dia", dayofmonth("data_ingestao"))

csv_df.printSchema()

df_dynamic_local = DynamicFrame.fromDF(csv_df, glueContext, "df_dyf_local")

glueContext.write_dynamic_frame.from_options(
    frame=df_dynamic_local,
    connection_type="s3",
    connection_options={
        "path": local_target_path,
        "partitionKeys": ["ano", "mes", "dia"]
    },
    format="parquet"
)

job.commit()