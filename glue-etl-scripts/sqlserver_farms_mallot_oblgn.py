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
    table_name="farms_mallot_oblgn",
    transformation_ctx="DataCatalogtable_node1",
)

# Script generated for node Change Schema
ChangeSchema_node2 = ApplyMapping.apply(
    frame=DataCatalogtable_node1,
    mappings=[
        ("sbmsn-cde", "long", "sbmsn_cde", "smallint"),
        ("purp-cde", "long", "purp_cde", "smallint"),
        ("oblgns-amt-cum", "double", "oblgns_amt_cum", "double"),
        ("oblgns-cnt-cum", "long", "oblgns_cnt_cum", "smallint"),
        ("vou-amt", "double", "vou_amt", "double"),
        ("ppb-cde-1st", "long", "ppb_cde_1st", "smallint"),
        ("ppb-cde-2-3", "long", "ppb_cde_2_3", "smallint"),
    ],
    transformation_ctx="ChangeSchema_node2",
)

# Script generated for node SQL Server table
SQLServertable_node3 = glueContext.write_dynamic_frame.from_catalog(
    frame=ChangeSchema_node2,
    database="synthetic-data",
    table_name="farm_account_dbo_farms_mallot_oblgn",
    transformation_ctx="SQLServertable_node3",
)

job.commit()
