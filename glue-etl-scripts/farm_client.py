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
    database="usda-eds-coe",
    table_name="eds_farm_farm_client",
    transformation_ctx="DataCatalogtable_node1",
)

# Script generated for node Change Schema
ChangeSchema_node1694807729398 = ApplyMapping.apply(
    frame=DataCatalogtable_node1,
    mappings=[
        ("case-nbr", "string", "case_nbr", "varchar"),
        ("case-nbr-oblr", "string", "case_nbr_oblr", "varchar"),
        ("mailg-lvl-client", "string", "mailg_ofc_client", "varchar"),
        ("mailg-cde-client", "string", "mailg_cde_client", "varchar"),
        ("nme-flds-borr-cnt", "long", "nme_flds_borr_cnt", "smallint"),
        ("adrs-flds-borr-cnt", "long", "adrs_flds_borr_cnt", "smallint"),
        ("nme-oblr", "string", "nme_oblr", "varchar"),
        ("nme-adrs-oblr-1", "string", "nme_adrs_oblr_1", "varchar"),
        ("nme-adrs-oblr-2", "string", "nme_adrs_oblr_2", "varchar"),
        ("nme-oblr-key", "string", "nme_oblr_key", "varchar"),
        ("nme-adrs-oblr-3", "string", "nme_adrs_city", "varchar"),
        ("nme-adrs-oblr-4", "string", "nme_adrs_ste", "varchar"),
        ("zip-cde", "long", "nme_adrs_zip_cde", "varchar"),
        ("race-desc-cde", "long", "race_desc_cde", "smallint"),
        ("sex-cde", "long", "sex_cde", "smallint"),
        ("mrtl-stat", "long", "mrtl_stat", "smallint"),
        ("tax-exempt-cde", "long", "tax_exempt_cde", "smallint"),
        ("vet-cde", "long", "vet_cde", "smallint"),
        ("due-day-pymt", "long", "due_day_pymt", "smallint"),
        ("applt-typ-cde", "long", "applt_typ_cde", "smallint"),
        ("net-worth-amt", "double", "net_worth_amt", "decimal"),
        ("ln-nbr-lst-asgd", "long", "ln_nbr_lst_asgd", "smallint"),
        ("rcrd-ln-cnt", "long", "rcrd_ln_cnt", "smallint"),
        ("ln-cnt-ee", "long", "ln_cnt_ee", "smallint"),
        ("ln-cnt-otc", "long", "ln_cnt_otc", "smallint"),
        ("ln-cnt-insrd-fo", "long", "ln_cnt_insrd_fo", "smallint"),
        ("ln-cnt-dir-fo", "long", "ln_cnt_dir_fo", "smallint"),
        ("ln-cnt-insrd-sw", "long", "ln_cnt_insrd_sw", "smallint"),
        ("ln-cnt-dir-sw", "long", "ln_cnt_dir_sw", "smallint"),
        ("ln-cnt-insrd-rh", "long", "ln_cnt_insrd_rh", "smallint"),
        ("ln-cnt-dir-rh", "long", "ln_cnt_dir_rh", "smallint"),
        ("ln-cnt-invstr", "long", "ln_cnt_invstr", "smallint"),
        ("ln-cnt-assoc", "long", "ln_cnt_assoc", "smallint"),
        ("susp-cde-acct", "long", "susp_cde_acct", "smallint"),
        ("dte-lst-rgstr-acct", "string", "dte_lst_rgstr_acct", "date"),
        ("rgstr-typ-lst-trnsctn", "long", "rgstr_typ_lst_trnsctn", "smallint"),
        ("sis-trf-cde", "string", "sis_trf_cde", "varchar"),
        ("empl-reltnshp-cde", "string", "empl_reltnshp_cde", "varchar"),
        ("lrtf-srvcg-cde", "long", "lrtf_srvcg_cde", "smallint"),
        ("mailg-ofc-fsa", "string", "mailg_ofc_fsa", "varchar"),
        ("mailg-cde-fsa", "string", "mailg_cde_fsa", "varchar"),
        ("orgztn-cde", "string", "orgztn_cde", "varchar"),
        ("dte-oac-estbd", "string", "dte_oac_estbd", "date"),
        ("dte-oac-rslvd", "string", "dte_oac_rslvd", "date"),
        ("dte-oac-mrtm-efctv", "string", "dte_oac_mrtm_efctv", "date"),
        ("prevl-indctr", "long", "prevl_indctr", "smallint"),
        ("nbr-complnts", "string", "nbr_complnts", "varchar"),
    ],
    transformation_ctx="ChangeSchema_node1694807729398",
)

# Script generated for node PostgreSQL
PostgreSQL_node1694807898775 = glueContext.write_dynamic_frame.from_catalog(
    frame=ChangeSchema_node1694807729398,
    database="usda-eds-coe",
    table_name="farm_loan_public_client",
    transformation_ctx="PostgreSQL_node1694807898775",
)

job.commit()
