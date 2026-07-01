from app.services.jd_parser import parse_jd
import json

jd_text = """
We are looking for a Senior Data Engineer to join our team.

Requirements:
- 4+ years of experience in data engineering
- Strong proficiency in Python and SQL
- Experience with Apache Airflow or similar orchestration tools
- Hands-on experience with AWS services (Redshift, S3, Glue, Lambda)
- Experience with dbt for data transformation
- Knowledge of Spark or PySpark
- Experience with Kafka or other streaming platforms

Preferred:
- Experience with Snowflake or BigQuery
- Knowledge of Terraform or infrastructure as code
- Familiarity with MLflow or ML pipelines
- Experience with Kubernetes or Docker

Responsibilities:
- Design and maintain scalable ETL/ELT pipelines
- Optimize data warehouse performance
- Collaborate with data science teams on ML pipelines
- Implement CI/CD for data workflows
"""

result = parse_jd(jd_text)
print(json.dumps(result, indent=2))