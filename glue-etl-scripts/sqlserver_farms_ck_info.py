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
    table_name="farms_ck_info",
    transformation_ctx="DataCatalogtable_node1",
)

# Script generated for node Change Schema
ChangeSchema_node2 = ApplyMapping.apply(
    frame=DataCatalogtable_node1,
    mappings=[
        ("rcrd-typ", "long", "rcrd_typ", "smallint"),
        ("fd-cde-2", "long", "fd_cde_2", "smallint"),
        ("nme-flds-borr-cnt", "long", "nme_flds_borr_cnt", "smallint"),
        ("mailg-lvl", "string", "mailg_lvl", "char"),
        ("st-ofc-mailg", "long", "st_ofc_mailg", "varchar"),
        ("cty-ofc-mailg", "long", "cty_ofc_mailg", "varchar"),
        ("dst-ofc-mailg", "long", "dst_ofc_mailg", "varchar"),
        ("st-cde-oblr", "long", "st_cde_oblr", "varchar"),
        ("cty-cde-oblr", "long", "cty_cde_oblr", "varchar"),
        ("id-nbr-oblr", "long", "id_nbr_oblr", "varchar"),
        ("ln-nbr", "long", "ln_nbr", "varchar"),
        ("cr-rept-fee-cde", "long", "cr_rept_fee_cde", "smallint"),
        ("nme-oblr", "string", "nme_oblr", "varchar"),
        ("advnc-multi-amt", "double", "advnc_multi_amt", "double"),
        ("dte-ck", "long", "dte_ck", "int"),
        ("aproptn-cde", "long", "aproptn_cde", "smallint"),
        ("geog-st-cde", "long", "geog_st_cde", "smallint"),
        ("fy", "long", "fy", "smallint"),
    ],
    transformation_ctx="ChangeSchema_node2",
)

# Script generated for node SQL Server table
SQLServertable_node3 = glueContext.write_dynamic_frame.from_catalog(
    frame=ChangeSchema_node2,
    database="synthetic-data",
    table_name="farm_account_dbo_farms_ck_info",
    transformation_ctx="SQLServertable_node3",
)

job.commit()
