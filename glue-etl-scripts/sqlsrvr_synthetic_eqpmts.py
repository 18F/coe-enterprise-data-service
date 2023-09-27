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
    table_name="eqpmts",
    transformation_ctx="DataCatalogtable_node1",
)

# Script generated for node Change Schema
ChangeSchema_node2 = ApplyMapping.apply(
    frame=DataCatalogtable_node1,
    mappings=[
        ("item-nbr", "long", "item_nbr", "smallint"),
        ("item-estd-cst", "double", "item_estd_cst", "decimal"),
        ("item-desc", "string", "item_desc", "varchar"),
        ("actl-nbr", "long", "actl_nbr", "bigint"),
        ("actl-amt", "long", "actl_amt", "bigint"),
        ("rqstd-nbr", "long", "rqstd_nbr", "bigint"),
        ("rqstd-amt", "long", "rqstd_amt", "bigint"),
        ("projd-nbr", "long", "projd_nbr", "bigint"),
        ("projd-amt", "long", "projd_amt", "bigint"),
    ],
    transformation_ctx="ChangeSchema_node2",
)

# Script generated for node SQL Server table
SQLServertable_node3 = glueContext.write_dynamic_frame.from_catalog(
    frame=ChangeSchema_node2,
    database="synthetic-data",
    table_name="farm_account_dbo_eqpmts",
    transformation_ctx="SQLServertable_node3",
)

job.commit()
