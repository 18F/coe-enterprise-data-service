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
    table_name="glmstr",
    transformation_ctx="DataCatalogtable_node1",
)

# Script generated for node Change Schema
ChangeSchema_node2 = ApplyMapping.apply(
    frame=DataCatalogtable_node1,
    mappings=[
        ("fy", "long", "fy", "smallint"),
        ("enty-cde", "long", "enty_cde", "smallint"),
        ("acct-nbr", "long", "acct_nbr", "smallint"),
        ("minor-cde", "long", "minor_cde", "smallint"),
        ("cur-mo-cde", "long", "cur_mo_cde", "smallint"),
        ("cur-acct-bal", "double", "cur_acct_bal", "string"),
        ("pr-yr-endg-bal", "double", "pr_yr_endg_bal", "string"),
        ("gl-mo-actv", "double", "gl_mo_actv", "string"),
        ("clsg-entries", "double", "clsg_entries", "string"),
        ("cur-mo-pr-yr-actv", "double", "cur_mo_pr_yr_actv", "string"),
        ("subq-mo-pr-yr-actv", "double", "subq_mo_pr_yr_actv", "string"),
        ("memo-acct-bal", "double", "memo_acct_bal", "string"),
        ("prev-bal-cntr", "double", "prev_bal_cntr", "string"),
        ("dte-lst-rgstr-acct", "long", "dte_lst_rgstr_acct", "int"),
        ("rgstr-typ-cde", "long", "rgstr_typ_cde", "smallint"),
        ("ctry-digit", "long", "ctry_digit", "smallint"),
    ],
    transformation_ctx="ChangeSchema_node2",
)

# Script generated for node SQL Server table
SQLServertable_node3 = glueContext.write_dynamic_frame.from_catalog(
    frame=ChangeSchema_node2,
    database="synthetic-data",
    table_name="farm_account_dbo_glmstr",
    transformation_ctx="SQLServertable_node3",
)

job.commit()
