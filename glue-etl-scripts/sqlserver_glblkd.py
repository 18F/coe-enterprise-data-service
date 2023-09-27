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
    table_name="glblkd",
    transformation_ctx="DataCatalogtable_node1",
)

# Script generated for node Change Schema
ChangeSchema_node2 = ApplyMapping.apply(
    frame=DataCatalogtable_node1,
    mappings=[
        ("acct-nbr", "long", "acct_nbr", "smallint"),
        ("minor-cde", "long", "minor_cde", "smallint"),
        ("fd-cde-2", "long", "fd_cde_2", "smallint"),
        ("fd-cde-3rd", "long", "fd_cde_3rd", "smallint"),
        ("fd-cde-4th", "long", "fd_cde_4th", "smallint"),
        ("trnsctn-cde", "long", "trnsctn_cde", "smallint"),
        ("dte-end-of-mo", "long", "dte_end_of_mo", "int"),
        ("purp-cde-1", "long", "purp_cde_1", "smallint"),
        ("dr-amt-indiv-gl-accts", "double", "dr_amt_indiv_gl_accts", "string"),
        ("cr-amt-indiv-gl-accts", "double", "cr_amt_indiv_gl_accts", "string"),
        ("mo-actv", "long", "mo_actv", "smallint"),
        ("rgstr-typ-cde", "long", "rgstr_typ_cde", "smallint"),
        ("time-stnds-data", "long", "time_stnds_data", "smallint"),
        ("user-inits", "string", "user_inits", "varchar"),
    ],
    transformation_ctx="ChangeSchema_node2",
)

# Script generated for node SQL Server table
SQLServertable_node3 = glueContext.write_dynamic_frame.from_catalog(
    frame=ChangeSchema_node2,
    database="synthetic-data",
    table_name="farm_account_dbo_glblkd",
    transformation_ctx="SQLServertable_node3",
)

job.commit()
