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
    table_name="glblkc",
    transformation_ctx="DataCatalogtable_node1",
)

# Script generated for node Change Schema
ChangeSchema_node2 = ApplyMapping.apply(
    frame=DataCatalogtable_node1,
    mappings=[
        ("fy", "long", "fy", "smallint"),
        ("enty-cde", "long", "enty_cde", "smallint"),
        ("blk-nbr-5", "long", "blk_nbr_5", "int"),
        ("sbsdry-acct-hash-ttl", "long", "sbsdry_acct_hash_ttl", "bigint"),
        ("acct-nbrs-hash-ttl", "long", "acct_nbrs_hash_ttl", "bigint"),
        ("minor-cde-hash-ttl", "long", "minor_cde_hash_ttl", "bigint"),
        ("dr-amt-indiv-gl-accts", "double", "dr_amt_indiv_gl_accts", "string"),
        ("cr-amt-indiv-gl-accts", "double", "cr_amt_indiv_gl_accts", "string"),
        ("user-inits", "string", "user_inits", "string"),
    ],
    transformation_ctx="ChangeSchema_node2",
)

# Script generated for node SQL Server table
SQLServertable_node3 = glueContext.write_dynamic_frame.from_catalog(
    frame=ChangeSchema_node2,
    database="synthetic-data",
    table_name="farm_account_dbo_glblkc",
    transformation_ctx="SQLServertable_node3",
)

job.commit()
