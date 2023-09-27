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
    database="synthetic-data2",
    table_name="farms_fd_side",
    transformation_ctx="DataCatalogtable_node1",
)

# Script generated for node Change Schema
ChangeSchema_node2 = ApplyMapping.apply(
    frame=DataCatalogtable_node1,
    mappings=[
        ("altmt", "double", "altmt", "double"),
        ("altmt-1st-acctg-prd", "double", "altmt_1st_acctg_prd", "double"),
        ("altmt-2nd-acctg-prd", "double", "altmt_2nd_acctg_prd", "double"),
        ("altmt-3rd-acctg-prd", "double", "altmt_3rd_acctg_prd", "double"),
        ("altmt-4th-acctg-prd", "double", "altmt_4th_acctg_prd", "double"),
    ],
    transformation_ctx="ChangeSchema_node2",
)

# Script generated for node SQL Server table
SQLServertable_node3 = glueContext.write_dynamic_frame.from_catalog(
    frame=ChangeSchema_node2,
    database="synthetic-data",
    table_name="farm_account_dbo_farms_fd_side",
    transformation_ctx="SQLServertable_node3",
)

job.commit()
