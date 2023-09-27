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
    table_name="farms_ck_info_frauds",
    transformation_ctx="DataCatalogtable_node1",
)

# Script generated for node Change Schema
ChangeSchema_node2 = ApplyMapping.apply(
    frame=DataCatalogtable_node1,
    mappings=[
        ("rcrd-typ", "long", "rcrd_typ", "smallint"),
        ("fd-cde-2", "long", "fd_cde_2", "smallint"),
        ("st-ofc-mailg", "long", "st_ofc_mailg", "smallint"),
        ("cty-ofc-mailg", "long", "cty_ofc_mailg", "smallint"),
        ("dst-ofc-mailg", "long", "dst_ofc_mailg", "varchar"),
        ("st-cde-oblr", "long", "st_cde_oblr", "smallint"),
        ("cty-cde-oblr", "long", "cty_cde_oblr", "smallint"),
        ("id-nbr-oblr", "long", "id_nbr_oblr", "varchar"),
        ("ln-nbr", "long", "ln_nbr", "smallint"),
        ("cr-rept-fee-cde", "long", "cr_rept_fee_cde", "varchar"),
        ("nme-oblr", "string", "nme_oblr", "varchar"),
        ("advnc-multi-amt", "double", "advnc_multi_amt", "double"),
        ("dte-ck", "long", "dte_ck", "int"),
        ("aproptn-cde", "long", "aproptn_cde", "smallint"),
        ("geog-st-cde", "long", "geog_st_cde", "smallint"),
        ("fy", "long", "fy", "smallint"),
        ("fed-resv-route-nbr", "long", "fed_resv_route_nbr", "string"),
        ("ck-digit-route-nbr", "long", "ck_digit_route_nbr", "smallint"),
        ("typ-bank-acct", "string", "typ_bank_acct", "char"),
        ("dpstr-acct-nbr", "string", "dpstr_acct_nbr", "varchar"),
        ("enty-cde", "long", "enty_cde", "smallint"),
        ("ck-cncltn-cde", "long", "ck_cncltn_cde", "smallint"),
        ("fnl-advnc-cde", "long", "fnl_advnc_cde", "smallint"),
        ("dte-lst-rgstr-dtl", "long", "dte_lst_rgstr_dtl", "int"),
        ("blk-nbr", "long", "blk_nbr", "smallint"),
    ],
    transformation_ctx="ChangeSchema_node2",
)

# Script generated for node SQL Server table
SQLServertable_node3 = glueContext.write_dynamic_frame.from_catalog(
    frame=ChangeSchema_node2,
    database="synthetic-data",
    table_name="farm_account_dbo_farms_ck_info_frauds",
    transformation_ctx="SQLServertable_node3",
)

job.commit()
