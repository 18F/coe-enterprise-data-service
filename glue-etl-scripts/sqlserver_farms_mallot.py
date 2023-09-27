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
    table_name="farms_mallot",
    transformation_ctx="DataCatalogtable_node1",
)

# Script generated for node Change Schema
ChangeSchema_node2 = ApplyMapping.apply(
    frame=DataCatalogtable_node1,
    mappings=[
        ("aproptn-cde", "long", "aproptn_cde", "smallint"),
        ("maj-cls", "long", "maj_cls", "smallint"),
        ("obj-clsfctn-cde", "long", "obj_clsfctn_cde", "smallint"),
        ("fy-acctg", "long", "fy_acctg", "smallint"),
        ("acct-typ-cde", "long", "acct_typ_cde", "smallint"),
        ("multi-elmt-cde", "long", "multi_elmt_cde", "smallint"),
        ("ok-to-proc-cde", "long", "ok_to_proc_cde", "smallint"),
        ("aprtnmts-cur-dtl", "double", "aprtnmts_cur_dtl", "string"),
        ("altmt-cur", "double", "altmt_cur", "string"),
        ("aprtnmt-typ", "long", "aprtnmt_typ", "smallint"),
        ("altmt-typ", "long", "altmt_typ", "smallint"),
        ("prd-cde", "long", "prd_cde", "smallint"),
        ("aprtnmts-1st-acctg-prd", "double", "aprtnmts_1st_acctg_prd", "string"),
        ("aprtnmts-2nd-acctg-prd", "double", "aprtnmts_2nd_acctg_prd", "string"),
        ("aprtnmts-3rd-acctg-prd", "double", "aprtnmts_3rd_acctg_prd", "string"),
        ("aprtnmts-4th-acctg-prd", "double", "aprtnmts_4th_acctg_prd", "string"),
    ],
    transformation_ctx="ChangeSchema_node2",
)

# Script generated for node SQL Server table
SQLServertable_node3 = glueContext.write_dynamic_frame.from_catalog(
    frame=ChangeSchema_node2,
    database="synthetic-data",
    table_name="farm_account_dbo_farms_mallot",
    transformation_ctx="SQLServertable_node3",
)

job.commit()
