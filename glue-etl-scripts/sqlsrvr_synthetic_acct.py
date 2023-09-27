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
    table_name="farms_acct_data",
    transformation_ctx="DataCatalogtable_node1",
)

# Script generated for node Change Schema
ChangeSchema_node2 = ApplyMapping.apply(
    frame=DataCatalogtable_node1,
    mappings=[
        ("ln-nbr", "long", "ln_nbr", "smallint"),
        ("fd-cde-2", "long", "fd_cde_2", "smallint"),
        ("fd-cde-3rd", "long", "fd_cde_3rd", "smallint"),
        ("fd-cde-4th", "long", "fd_cde_4th", "smallint"),
        ("kind-cde-ln", "long", "kind_cde_ln", "smallint"),
        ("int-rate-note", "double", "int_rate_note", "decimal"),
        ("int-rate-note-1st", "double", "int_rate_note_1st", "decimal"),
        ("pymt-typ-cde", "long", "pymt_typ_cde", "smallint"),
        ("dir-pymt-cde", "long", "dir_pymt_cde", "smallint"),
        ("dte-amortn-efctv", "long", "dte_amortn_efctv", "varchar"),
        ("dstr-typ-cde", "long", "dstr_typ_cde", "smallint"),
        ("fy-dstr-dclrd", "long", "fy_dstr_dclrd", "smallint"),
        ("dstr-dclrd-nbr", "long", "dstr_dclrd_nbr", "smallint"),
        ("mrg-cntrl", "long", "mrg_cntrl", "smallint"),
        ("docmt-typ-cde", "string", "docmt_typ_cde", "string"),
        ("dte-oblgn-ln", "long", "dte_oblgn_ln", "varchar"),
        ("asstnc-typ-cde", "long", "asstnc_typ_cde", "smallint"),
        ("ln-amt-oblgn", "double", "ln_amt_oblgn", "decimal"),
        ("begng-frmr-rnchr-cde", "string", "begng_frmr_rnchr_cde", "string"),
        ("colltl-cde", "long", "colltl_cde", "smallint"),
        ("cpn-procg-dte", "long", "cpn_procg_dte", "varchar"),
        ("case-nbr-chng-cde", "long", "case_nbr_chng_cde", "smallint"),
        ("pymt-asstnc-meth-cde", "long", "pymt_asstnc_meth_cde", "smallint"),
        ("int-rate-prev", "double", "int_rate_prev", "decimal"),
        ("int-rate-prev-redfnd", "double", "int_rate_prev_redfnd", "decimal"),
    ],
    transformation_ctx="ChangeSchema_node2",
)

# Script generated for node SQL Server table
SQLServertable_node3 = glueContext.write_dynamic_frame.from_catalog(
    frame=ChangeSchema_node2,
    database="synthetic-data",
    table_name="farm_account_dbo_acct_test",
    transformation_ctx="SQLServertable_node3",
)

job.commit()
