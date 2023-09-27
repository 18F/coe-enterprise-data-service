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
    table_name="glacct",
    transformation_ctx="DataCatalogtable_node1",
)

# Script generated for node Change Schema
ChangeSchema_node2 = ApplyMapping.apply(
    frame=DataCatalogtable_node1,
    mappings=[
        ("acct-nbr", "long", "acct_nbr", "smallint"),
        ("prfx-line-nbr", "long", "prfx_line_nbr", "smallint"),
        ("sfx-line-nbr", "long", "sfx_line_nbr", "varchar"),
        ("sub-sfx-line-nbr", "long", "sub_sfx_line_nbr", "smallint"),
        ("minor-cde-flag", "long", "minor_cde_flag", "smallint"),
        ("acct-title", "string", "acct_title", "string"),
        ("bal-cde", "long", "bal_cde", "smallint"),
        ("enty", "long", "enty", "smallint"),
        ("dte-lst-rgstr-acct", "long", "dte_lst_rgstr_acct", "int"),
    ],
    transformation_ctx="ChangeSchema_node2",
)

# Script generated for node SQL Server table
SQLServertable_node3 = glueContext.write_dynamic_frame.from_catalog(
    frame=ChangeSchema_node2,
    database="synthetic-data",
    table_name="farm_account_dbo_glacct",
    transformation_ctx="SQLServertable_node3",
)

job.commit()
