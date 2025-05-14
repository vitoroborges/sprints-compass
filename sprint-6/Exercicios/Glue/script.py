import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import count, col, desc, upper, trim, sum
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_OUTPUT_PATH'])

source_file = args["S3_INPUT_PATH"]
target_path = args["S3_OUTPUT_PATH"]

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

df = glueContext.create_dynamic_frame.from_options(
    "s3",
    {
        "paths": [
            source_file
            ]
    },
    "csv",
    {"withHeader": True, "separator": ","},
    )
    
df.printSchema()

df = df.toDF()

df = df.toDF(*[c.upper() for c in df.columns])

df = df.withColumn("NOME", upper(trim(col("NOME"))))
df = df.withColumn("SEXO", trim(col("SEXO")))
df = df.withColumn("ANO", trim(col("ANO")).cast("int"))
df = df.withColumn("TOTAL", trim(col("TOTAL")).cast("int"))

df.printSchema()

print("Número de linhas no dataframe: ", df.count())

df_agrupado = df.groupBy("ANO", "SEXO").agg(sum("TOTAL").alias("qtd_nomes"))
df_ordenado = df_agrupado.orderBy(col("ANO").desc())
df_ordenado.show()

df_feminino = df.filter(col("SEXO") == "F")
df_ordenado_f = df_feminino.orderBy(col("TOTAL").desc())
df_ordenado_f.show(1)

df_masculino = df.filter(col("SEXO") == "M")
df_ordenado_m = df_masculino.orderBy(col("TOTAL").desc())
df_ordenado_m.show(1)

df.write\
    .mode("overwrite")\
    .partitionBy("SEXO", "ANO")\
    .format("json")\
    .save(target_path)

job.commit()