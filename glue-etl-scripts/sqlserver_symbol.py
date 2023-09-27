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
    table_name="symbol",
    transformation_ctx="DataCatalogtable_node1",
)

# Script generated for node Change Schema
ChangeSchema_node2 = ApplyMapping.apply(
    frame=DataCatalogtable_node1,
    mappings=[
        ("trsry-sym", "string", "trsry_sym", "string"),
        ("acct-mo", "long", "acct_mo", "smallint"),
        ("dept-nbr", "long", "dept_nbr", "smallint"),
        ("srvc-agcy", "string", "srvc_agcy", "varchar"),
        ("agcy", "string", "agcy", "varchar"),
        ("acct-statn", "string", "acct_statn", "varchar"),
        ("fd-cde-2", "long", "fd_cde_2", "smallint"),
        ("fd-cde-3rd", "long", "fd_cde_3rd", "smallint"),
        ("fd-cde-4th", "long", "fd_cde_4th", "smallint"),
        ("trnsmt", "string", "trnsmt", "string"),
        ("trnsmt-dte", "long", "trnsmt_dte", "int"),
    ],
    transformation_ctx="ChangeSchema_node2",
)

# Script generated for node Data Catalog table
DataCatalogtable_node3 = glueContext.write_dynamic_frame.from_catalog(
    frame=ChangeSchema_node2,
    database="synthetic-data",
    table_name="farm_account_dbo_symbol",
    transformation_ctx="DataCatalogtable_node3",
)

job.commit()
