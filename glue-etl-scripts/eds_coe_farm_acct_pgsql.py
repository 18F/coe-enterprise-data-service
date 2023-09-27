import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import to_timestamp, to_date, date_format


args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Data Catalog table
DataCatalogtable_node1 = glueContext.create_dynamic_frame.from_catalog(
    database="usda-eds-coe",
    table_name="accountfarm_account",
    transformation_ctx="DataCatalogtable_node1",
)

# Script generated for node ApplyMapping
ApplyMapping_node2 = ApplyMapping.apply(
    frame=DataCatalogtable_node1,
    mappings=[
        ("ln_nbr", "long", "ln_nbr", "long"),
        ("fd_cde", "long", "fd_cde", "long"),
        ("kind_cde_ln", "long", "kind_cde_ln", "long"),
        ("int_rate_note", "double", "int_rate_note", "double"),
        ("int_rate_note_1st", "double", "int_rate_note_1st", "double"),
        ("pymt_typ_cde", "long", "pymt_typ_cde", "long"),
        ("dir_pymt_cde", "long", "dir_pymt_cde", "long"),
        ("dte_amortn_efctv", "string", "dte_amortn_efctv", "date"),
        ("dstr_dclrd_cde", "long", "dstr_dclrd_cde", "long"),
        ("mrg_cntrl", "long", "mrg_cntrl", "long"),
        ("docmt_typ_cde", "string", "docmt_typ_cde", "string"),
        ("dte_oblgn_ln", "string", "dte_oblgn_ln", "date"),
        ("asstnc_typ_cde", "long", "asstnc_typ_cde", "long"),
        ("ln_amt_oblgn", "double", "ln_amt_oblgn", "double"),
        ("begng_frmr_rnchr_cde", "string", "begng_frmr_rnchr_cde", "string"),
        ("colltl_cde", "long", "colltl_cde", "long"),
        ("cpn_procg_dte", "string", "cpn_procg_dte", "date"),
        ("case_nbr_chng_cde", "long", "case_nbr_chng_cde", "long"),
        ("pymt_asstnc_meth_cde", "long", "pymt_asstnc_meth_cde", "long"),
        ("int_rate_prev", "double", "int_rate_prev", "double"),
        ("int_rate_prev_redfnd", "double", "int_rate_prev_redfnd", "double"),
    ],
    transformation_ctx="ApplyMapping_node2",
)

# Script generated for node PostgreSQL table
PostgreSQLtable_node3 = glueContext.write_dynamic_frame.from_catalog(
    frame=ApplyMapping_node2,
    database="usda-eds-coe",
    table_name="farm_loan_public_acct_data",
    transformation_ctx="PostgreSQLtable_node3",
)

job.commit()
