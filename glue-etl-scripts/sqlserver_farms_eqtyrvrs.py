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
    table_name="farms_eqtyrvrs",
    transformation_ctx="DataCatalogtable_node1",
)

# Script generated for node Change Schema
ChangeSchema_node2 = ApplyMapping.apply(
    frame=DataCatalogtable_node1,
    mappings=[
        ("dte-trnsctn", "long", "dte_trnsctn", "int"),
        ("ln-nbr", "long", "ln_nbr", "smallint"),
        ("ln-nbr-new", "long", "ln_nbr_new", "smallint"),
        ("fd-cde-2", "long", "fd_cde_2", "smallint"),
        ("fd-cde-3rd", "long", "fd_cde_3rd", "smallint"),
        ("fd-cde-4th", "long", "fd_cde_4th", "smallint"),
        ("amortn-amt-cum", "double", "amortn_amt_cum", "double"),
        ("prtl-sale-ln-nbr", "long", "prtl_sale_ln_nbr", "smallint"),
        ("prtl-sale-amortn-amt", "double", "prtl_sale_amortn_amt", "double"),
    ],
    transformation_ctx="ChangeSchema_node2",
)

# Script generated for node SQL Server table
SQLServertable_node3 = glueContext.write_dynamic_frame.from_catalog(
    frame=ChangeSchema_node2,
    database="synthetic-data",
    table_name="farm_account_dbo_farms_eqtyrvrs",
    transformation_ctx="SQLServertable_node3",
)

job.commit()
