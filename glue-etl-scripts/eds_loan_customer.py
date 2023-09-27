import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Data Catalog table
DataCatalogtable_node1 = glueContext.create_dynamic_frame.from_catalog(
    database="usda-eds-coe",
    table_name="loan_customercustomer_data_csv",
    transformation_ctx="DataCatalogtable_node1",
)

# Script generated for node ApplyMapping
ApplyMapping_node2 = ApplyMapping.apply(
    frame=DataCatalogtable_node1,
    mappings=[
        ("country", "string", "country", "string"),
        ("loan_effective_date", "string", "loan_effective_date", "date"),
        ("address", "string", "address", "string"),
        ("gender", "string", "gender", "string"),
        ("city", "string", "city", "string"),
        ("birth_date", "string", "birth_date", "date"),
        ("ssn", "string", "ssn_id", "string"),
        ("loan_amount", "double", "loan_amount", "decimal"),
        ("loan_number", "long", "loan_number", "long"),
        ("registered_at", "string", "registered_timestamp", "timestamp"),
        ("email", "string", "customer_email", "string"),
        ("interest_rate", "double", "interest_rate", "decimal"),
        ("name", "string", "customer_name", "string"),
        ("phone", "string", "customer_phone_nbr", "string"),
    ],
    transformation_ctx="ApplyMapping_node2",
)

# Script generated for node PostgreSQL
PostgreSQL_node1692298626935 = glueContext.write_dynamic_frame.from_catalog(
    frame=ApplyMapping_node2,
    database="usda-eds-coe",
    table_name="farm_loan_public_loan_customer",
    transformation_ctx="PostgreSQL_node1692298626935",
)

job.commit()
