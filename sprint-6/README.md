# Sprint 6
## Resumo
**AWS Glue Getting Started:** O AWS Glue Getting Started ensina o básico pra começar a usar o Glue, que é uma ferramenta da AWS pra organizar e transformar dados. No guia, a gente aprende como usar um crawler pra encontrar dados e criar uma tabela automática, e depois como montar um job pra transformar esses dados. É tipo um passo a passo pra entender como automatizar o processo de ETL na nuvem.


**Fundamentals of Analytics on AWS – Part 2:** Esse conteúdo mostra como montar uma solução de análise de dados na AWS, usando serviços integrados pra transformar dados brutos em insights, de forma escalável e econômica. É a continuação da parte 1, focando mais no processamento e na visualização dos dados.

## Desafio
[Link para o desafio](./Desafio/README.md)

## Exercicios

### Spark
[Link para o notebook](./Exercicios/PySpark/exercicio.ipynb)

Executei o exercicio no container da sprint passada. 

Gerei os nomes e fiz o processamento com o pyspark. Fiquei espantado com a velocidade de processamento.

![Spark Script 1](./Exercicios/Evidencias/spark-script-exercicio.png)
![Spark Script Output](./Exercicios/Evidencias/spark-script-output.png)
![Spark Script 2](./Exercicios/Evidencias/spark-script-2-exercicio.png)
![Spark Script Output 2](./Exercicios/Evidencias/spark-script-output-2.png)
![Spark Script 3](./Exercicios/Evidencias/spark-script-3.png)
![Spark Script Output 3](./Exercicios/Evidencias/spark-script-output-3-nomes.png)
![Spark Sql Output](./Exercicios/Evidencias/spark-script-output-3-sql.png)

### Glue
[Link para o script](./Exercicios/Glue/script.py)

Nesse exercício eu criei o meu primeiro job no glue.

A ferramenta que implementa o spark se mostrou de grande importância para os processos de ETL.

![Glue Script 1](./Exercicios/Evidencias/glue-numero-linhas.png)
![Glue Script 2](./Exercicios/Evidencias/glue-renomear-coluna.png)
![Glue Script 3](./Exercicios/Evidencias/glue-log-maior-f.png)
![Glue Script 4](./Exercicios/Evidencias/glue-log-maior-m.png)
![Glue Script 5](./Exercicios/Evidencias/glue-log-mf.png)
![Glue Script 6](./Exercicios/Evidencias/glue-exercicio-ouput.png)
![Glue Crawler](./Exercicios/Evidencias/glue-crawler-criado.png)
![Glue Query](./Exercicios/Evidencias/glue-sql-script-exercicio.png)
![Glue Sql](./Exercicios/Evidencias/glue-sql-tabela.png)