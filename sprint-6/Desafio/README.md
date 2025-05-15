# Desafio
[Link para o video](https://compasso-my.sharepoint.com/:v:/g/personal/vitor_borges_pb_compasso_com_br/EXY4JMqpsH9OvlGmuQDWTgoBB2VqTt5LFjmkQnCp8w_lHw?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D&e=Aub7Dg)
# Etapa 1
[Link para o script](../Desafio/Etapa1/glue_csv.py)

Na primeira etapa, tratamos os dados em formato csv na camada raw do s3 bucket, aonde está localizado nosso datalake.

Para a role que dará permissão de acesso ao glue e demais componentes, reutilizarei o **AWSGlueServiceRole-Lab4** do exercício.

![Aws Role](../Evidencias/iam-role.png)

Iniciamos criando um job no AWS Glue, onde executaremos as instruções necessárias para a transformação dos dados para o formato parquet.

![Glue job](../Evidencias/glue-job-desafio.png)

Importamos nosso conjunto de csv e transformamos em um dataframe spark glue.

Retiramos espaços em branco do nome das colunas, eliminamos os dados duplicados e adicionamos 3 novas colunas que serão fundamentais para o particionamento dos nossos dados.

Os dados serão particionados por ano, mês e dia.

![Glue Script 1](../Evidencias/glue-csv-script1.png)

Após isso, exibimos o schema para garantir a integridade dos dados.

E, por fim, transformamos nosso data frame para um tabela dinâmica do próprio glue.

![Glue Script 2](../Evidencias/glue-csv-script2.png)

Executado o script, nosso s3 ficará assim:

![Glue Trusted CSV](../Evidencias/glue-trusted-csv.png)

## Etapa 2
[Link para o script](../Desafio/Etapa2/glue_json.py)

Nessa etapa, importaremos os arquivos json que foram extraidos via api tmdb na sprint passada.

Todos os arquivos estão armazenados na camada raw, e separados por data de requisição.

Usamos o spark para criar um datafame json bruto.

![Glue Json Script](../Evidencias/glue-json-script.png)

Após isso, tratamos os dados para incluir ano, mês e dia. Isso nos auxiliara no momento do particionamento dos dados.

![Glue Json Script 2](../Evidencias/glue-json-script2.png)

Transformamos nosso dataframe em um tabela dinâmica e posteriormente, criamos as partições na camada trusted.

![Glue Json Script 3](../Evidencias/glue-json-scrip3.png)

No fim, a nossa camada trusted ficou desse jeito:

![Glue Trusted JSON](../Evidencias/glue-trusted-json.png)

Seguindo as normas propostas pelo desafio!


