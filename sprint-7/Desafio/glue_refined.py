import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import col, lit, regexp_replace, when
from datetime import datetime

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'INPUT_PATH_TMDB', 'INPUT_PATH_LOCAL', 'OUTPUT_PATH'])
INPUT_PATH_LOCAL = args['INPUT_PATH_LOCAL']
INPUT_PATH_TMDB = args['INPUT_PATH_TMDB']
OUTPUT_PATH = args['OUTPUT_PATH']

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

today = datetime.now()
year = today.year
month = today.month
day = today.day

df_movies = spark.read.parquet(f"{INPUT_PATH_TMDB}/movies/")
df_companies = spark.read.parquet(f"{INPUT_PATH_TMDB}/production_companies/")
df_genres = spark.read.parquet(f"{INPUT_PATH_TMDB}/genres/")
df_countries = spark.read.parquet(f"{INPUT_PATH_TMDB}/production_countries/")
df_durations = spark.read.parquet(INPUT_PATH_LOCAL)

# Dimensão Filme
dim_movie = df_movies.select(
    col("id").alias("movie_id"),
    col("title"),
    col("release_date")
).dropDuplicates(["movie_id"])

# Dimensão Empresa
dim_company = df_companies.select(
    col("company_id"),
    col("company_name")
).dropDuplicates(["company_id"])

# Dimensão Gênero
dim_genre = df_genres.select(
    col("genre_id"),
    col("genre_name")
).dropDuplicates(["genre_id"])

# Dimensão País
dim_country = df_countries.select(
    col("country_code"),
    col("country_name")
).dropDuplicates(["country_code"])

# Unificando tabelas por movie_id
fact_table = df_movies.select(
    col("id").alias("movie_id"),
    col("popularity"),
    col("vote_average"),
    col("year")
).join(df_durations.select(
    "movie_id", "duration_min", "vote_quantity"
), "movie_id", "left") \
.join(df_genres.select(
    "movie_id", "genre_id"
), "movie_id", "left") \
.join(df_companies.select(
    "movie_id", "company_id"
), "movie_id", "left") \
.join(df_countries.select(
    "movie_id", "country_code"
), "movie_id", "left") \
.withColumn("year", lit(year)) \
.withColumn("month", lit(month)) \
.withColumn("day", lit(day))

fact_table = fact_table.dropDuplicates()

# Convertendo para DynamicFrame e salvando particionado
for dim_name, df in [("dim_movie", dim_movie), 
                     ("dim_company", dim_company), 
                     ("dim_genre", dim_genre), 
                     ("dim_country", dim_country)]:
    
    dyf = DynamicFrame.fromDF(df, glueContext, dim_name)
    
    glueContext.write_dynamic_frame.from_options(
        frame=dyf,
        connection_type="s3",
        connection_options={
            "path": f"{OUTPUT_PATH}/{dim_name}/",
            "partitionKeys": []
        },
        format="parquet"
    )

# Escrevendo a tabela fato
fact_dyf = DynamicFrame.fromDF(fact_table, glueContext, "movies_fact")

glueContext.write_dynamic_frame.from_options(
    frame=fact_dyf,
    connection_type="s3",
    connection_options={
        "path": f"{OUTPUT_PATH}/movies_fact/",
        "partitionKeys": ["year", "month", "day"]
    },
    format="parquet"
)
job.commit()