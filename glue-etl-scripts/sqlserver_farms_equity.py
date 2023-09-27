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
    table_name="farms_equity",
    transformation_ctx="DataCatalogtable_node1",
)

# Script generated for node Change Schema
ChangeSchema_node2 = ApplyMapping.apply(
    frame=DataCatalogtable_node1,
    mappings=[
        ("fd-cde-2", "long", "fd_cde_2", "smallint"),
        ("fd-cde-3rd", "long", "fd_cde_3rd", "smallint"),
        ("fd-cde-4th", "long", "fd_cde_4th", "smallint"),
        ("ln-nbr", "long", "ln_nbr", "smallint"),
        ("typ-plan-cde", "long", "typ_plan_cde", "smallint"),
        ("wrtdwn-amt-scrd-re", "double", "wrtdwn_amt_scrd_re", "double"),
        ("wrtdwn-amt-not-scrd-re", "double", "wrtdwn_amt_not_scrd_re", "double"),
        ("begng-mkt-vlu", "double", "begng_mkt_vlu", "double"),
        ("endg-mkt-vlu", "double", "endg_mkt_vlu", "double"),
        ("net-recvry-vlu", "double", "net_recvry_vlu", "double"),
        ("potl-recptr-amt", "double", "potl_recptr_amt", "double"),
        ("rcvb-amt-due", "double", "rcvb_amt_due", "double"),
        ("rcvb-amt-pd", "double", "rcvb_amt_pd", "double"),
        ("dte-efctv", "long", "dte_efctv", "int"),
        ("dte-mturty", "long", "dte_mturty", "int"),
        ("dte-lst-csh", "long", "dte_lst_csh", "int"),
        ("dte-fnl-pymt", "long", "dte_fnl_pymt", "int"),
        ("dte-lst-rgstr-dtl", "long", "dte_lst_rgstr_dtl", "int"),
        ("rgstr-typ-lst-trnsctn", "long", "rgstr_typ_lst_trnsctn", "smallint"),
        ("equity-sale-contr", "long", "equity_sale_contr", "smallint"),
        ("appltn-cde", "string", "appltn_cde", "varchar"),
        ("fully-pd-cde", "string", "fully_pd_cde", "varchar"),
        ("fnl-rcvb-cde", "long", "fnl_rcvb_cde", "smallint"),
        ("dte-sale-prop", "long", "dte_sale_prop", "int"),
        ("dte-compld-srvcg-appltn", "long", "dte_compld_srvcg_appltn", "int"),
        ("asstnc-typ-cde", "long", "asstnc_typ_cde", "smallint"),
        ("dte-oblgn", "long", "dte_oblgn", "int"),
        ("cr-appld-noncsh", "double", "cr_appld_noncsh", "string"),
        ("dte-lst-noncsh", "long", "dte_lst_noncsh", "int"),
        ("susp-cde", "long", "susp_cde", "smallint"),
    ],
    transformation_ctx="ChangeSchema_node2",
)

# Script generated for node SQL Server table
SQLServertable_node3 = glueContext.write_dynamic_frame.from_catalog(
    frame=ChangeSchema_node2,
    database="synthetic-data",
    table_name="farm_account_dbo_farms_equity",
    transformation_ctx="SQLServertable_node3",
)

job.commit()
