
CREATE DATABASE fsa_coe_eds OWNER awsuser;

CREATE SCHEMA IF NOT EXISTS farms authorization awsuser;



CREATE TABLE IF NOT EXISTS farms.acct_data
( 
	ln_nbr               SMALLINT  not NULL primary KEY,
	fd_cde_2             SMALLINT  NULL ,
	fd_cde_3rd           SMALLINT  NULL ,
	fd_cde_4th           SMALLINT  NULL ,
	kind_cde_ln          SMALLINT  NULL ,
	int_rate_note_1st    NUMERIC(6,6)  NULL ,
	pymt_typ_cde         SMALLINT  NULL ,
	dir_pymt_cde         SMALLINT  NULL ,
	dte_amortn_efctv     INTEGER  NULL ,
	dstr_typ_cde         SMALLINT  NULL ,
	fy_dstr_dclrd        SMALLINT  NULL ,
	dstr_dclrd_nbr       SMALLINT  NULL ,
	mrg_cntrl            SMALLINT  NULL ,
	docmt_typ_cde        CHAR(1)  NULL ,
	dte_oblgn_ln         INTEGER  NULL ,
	asstnc_typ_cde       SMALLINT  NULL ,
	ln_amt_oblgn         NUMERIC(10,2)  NULL ,
	begng_frmr_rnchr_cde CHAR(1)  NULL ,
	colltl_cde           SMALLINT  NULL ,
	cpn_procg_dte        INTEGER  NULL ,
	case_nbr_chng_cde    SMALLINT  NULL ,
	pymt_asstnc_meth_cde SMALLINT  NULL ,
	int_rate_prev_redfnd NUMERIC(6,6)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.acqd_prop
( 
	fd_cde_2_acqd_prop   SMALLINT  NULL ,
	fd_cde_3rd_acqd_prop SMALLINT  NULL ,
	fd_cde_4th_acqd_prop SMALLINT  NULL ,
	ascs_frm_nbr_1       VARCHAR(7)  NULL ,
	ascs_frm_nbr_2       VARCHAR(7)  NULL ,
	st_cde_acqd_prop     SMALLINT  NULL ,
	cty_cde_acqd_prop    SMALLINT  NULL ,
	advc_nbr             INTEGER  NULL ,
	mailg_lvl_acqd       CHAR(1)  NULL ,
	st_ofc_mailg_acqd    SMALLINT  NULL ,
	dst_ofc_mailg_acqd   SMALLINT  NULL ,
	dte_lst_csh_cr_prop  INTEGER  NULL ,
	dte_acqstn           INTEGER  NULL ,
	lqdtn_cde            SMALLINT  NULL ,
	vlu_acqstn           NUMERIC(10,2)  NULL ,
	acres_cnt            NUMERIC(7,1)  NULL ,
	prin_cr_acqstn       NUMERIC(10,2)  NULL ,
	int_cr_acqstn        NUMERIC(9,2)  NULL ,
	prin_unpd_prop_acqstn NUMERIC(10,2)  NULL ,
	int_unpd_prop_acqstn NUMERIC(9,2)  NULL ,
	cptl_imprvmts        NUMERIC(9,2)  NULL ,
	dte_1st_advtsd       INTEGER  NULL ,
	incm_oth_acqd_prop   NUMERIC(9,2)  NULL ,
	acqd_prop_gain_loss_fnl_sale NUMERIC(9,2)  NULL ,
	dte_jdgmt            INTEGER  NULL ,
	jdgmt_amt            NUMERIC(9,2)  NULL ,
	dte_wrtf             INTEGER  NULL ,
	wrtf_unpd_prin       NUMERIC(9,2)  NULL ,
	wrtf_unpd_int_amt    NUMERIC(9,2)  NULL ,
	dte_sale_prop        INTEGER  NULL ,
	acqd_prop_sale_amt   NUMERIC(10,2)  NULL ,
	sale_prtl_compl_cde  SMALLINT  NULL ,
	nme_purchr           VARCHAR(19)  NULL ,
	st_cde_purchr        SMALLINT  NULL ,
	cty_cde_purchr       SMALLINT  NULL ,
	id_nbr_purchr        NUMERIC(10)  NULL ,
	dte_acqstn_procd     SMALLINT  NULL ,
	dte_sale_procd       SMALLINT  NULL ,
	dlt_cde              SMALLINT  NULL ,
	fd_cde_acqd_prop_pr_acqstn SMALLINT  NULL ,
	susp_cde_acqd_prop   SMALLINT  NULL ,
	dte_lst_rgstr_dtl_prop INTEGER  NULL ,
	rgstr_typ_lst_chng_prop SMALLINT  NULL ,
	dte_acqstn_sbmtd_mo  SMALLINT  NULL ,
	dte_acqstn_sbmtd_day SMALLINT  NULL ,
	dte_acqstn_sbmtd_yr  SMALLINT  NULL ,
	prop_loctn           VARCHAR(16)  NULL ,
	prop_desc_cde        SMALLINT  NULL ,
	prop_sutblty         SMALLINT  NULL ,
	orig_mkt_vlu         NUMERIC(9,2)  NULL ,
	typ_bus              SMALLINT  NULL ,
	cur_mkt_vlu          NUMERIC(9,2)  NULL ,
	dte_lst_apprsl_mo    SMALLINT  NULL ,
	dte_lst_apprsl_day   SMALLINT  NULL ,
	dte_lst_apprsl_yr    SMALLINT  NULL ,
	acres_acqd_crop      NUMERIC(6,1)  NULL ,
	acres_acqd_pstr      NUMERIC(6,1)  NULL ,
	acres_acqd_wdlnd     NUMERIC(6,1)  NULL ,
	acres_acqd_oth       NUMERIC(6,1)  NULL ,
	dte_cr_sale_compld_mo SMALLINT  NULL ,
	dte_cr_sale_compld_day SMALLINT  NULL ,
	dte_cr_sale_compld_yr SMALLINT  NULL ,
	typ_sale_dspsl       SMALLINT  NULL ,
	term_sale_dspsl      SMALLINT  NULL ,
	purchr_typ_cde       SMALLINT  NULL ,
	sd_applt_cde         CHAR(1)  NULL ,
	dte_fld_notfs_fws    INTEGER  NULL ,
	dte_fws_rqsts_easmnt INTEGER  NULL ,
	borr_rhts_wavd       CHAR(1)  NULL ,
	prop_mngr            VARCHAR(19)  NULL ,
	dte_mngmt_agrmt      INTEGER  NULL ,
	exprtn_dte_mngmt_agrmt INTEGER  NULL ,
	dte_2nd_advtsd       INTEGER  NULL ,
	sales_commsn         NUMERIC(8,2)  NULL ,
	oth_sellg_exp        NUMERIC(8,2)  NULL ,
	prop_street_adrs     VARCHAR(16)  NULL ,
	prop_listd_mo        SMALLINT  NULL ,
	prop_listd_day       SMALLINT  NULL ,
	prop_listd_yr        SMALLINT  NULL ,
	gain_loss_acqstn     NUMERIC(9,2)  NULL ,
	gr_sale_amt          NUMERIC(10,2)  NULL ,
	dte_subdvsn          INTEGER  NULL ,
	subq_dte_subdvsn     INTEGER  NULL ,
	pr_prop_id           INTEGER  NULL ,
	purchr_race_cde      SMALLINT  NULL ,
	purchr_kind_cde      SMALLINT  NULL ,
	purchr_reltnshp_cde  SMALLINT  NULL ,
	dwnpymt_sbmtd        NUMERIC(9,2)  NULL ,
	dwnpymt_crdtd        NUMERIC(9,2)  NULL ,
	net_csh_sale_crdtd   NUMERIC(10,2)  NULL ,
	net_csh_sale_rcvb    NUMERIC(10,2)  NULL ,
	net_dwnpymt_rcvb     NUMERIC(9,2)  NULL ,
	asstnc_typ_cde_acqd  SMALLINT  NULL ,
	dte_oblgn_ln_acqd    INTEGER  NULL ,
	ln_nbr_scrd_acqd     SMALLINT  NULL ,
	acqd_prop_oprtg_cst_fmha NUMERIC(8,2)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.adps_cntrl
( 
	adps_cntrl_key       CHAR(2)  NULL ,
	adps_seqnc_nbr       INTEGER  NULL ,
	dte_julian           INTEGER  NULL  
);

CREATE TABLE IF NOT EXISTS farms.advance
( 
	chgs_advnc_from_fd   NUMERIC(9,2)  NULL ,
	prin_cr_advnc_from_fd NUMERIC(9,2)  NULL ,
	int_cr_advnc_from_fd NUMERIC(9,2)  NULL ,
	int_fcl_from_advnc_dte NUMERIC(9,2)  NULL ,
	sched_stat_advnc_from_fd NUMERIC(9,2)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.aid
( 
	dte_dfrl_efctv       INTEGER  NULL ,
	dte_dfrl_exprtn      INTEGER  NULL ,
	dte_dfrl_cncltn      INTEGER  NULL ,
	stat_dfrl            SMALLINT  NULL ,
	dte_set_aside_efctv  INTEGER  NULL ,
	dte_set_aside_exprtn INTEGER  NULL ,
	dte_set_aside_cncltn INTEGER  NULL ,
	debt_set_aside_ttl_amt NUMERIC(8,2)  NULL ,
	stat_debt_set_aside  SMALLINT  NULL ,
	dte_mrtm_efctv_rh    INTEGER  NULL ,
	dte_mrtm_cncltn_rh   INTEGER  NULL ,
	mrtm_renwl_nbr_rh    SMALLINT  NULL ,
	stat_mrtm_rh         SMALLINT  NULL ,
	nbr_dfrl_renwls      SMALLINT  NULL ,
	dfrd_int_ttl_amt     NUMERIC(9,2)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.altmadj
( 
	vou_yr               SMALLINT  NULL ,
	vou_mo               SMALLINT  NULL ,
	vou_day              SMALLINT  NULL ,
	vou_nbr              INTEGER  NULL ,
	trnsctn_cde_updte    CHAR(2)  NULL ,
	blk_nbr              SMALLINT  NULL ,
	dte_blk_proc_ctry    NUMERIC(8)  NULL ,
	stat_cde             SMALLINT  NULL ,
	updte_cde_gl         CHAR(1)  NULL ,
	prepr_init           VARCHAR(4) NULL ,
	addtnl_rmrks         VARCHAR(48)  NULL ,
	adjmt_user_id        VARCHAR(6)  NULL ,
	nbr_of_occurs        SMALLINT  NULL ,
	fy                   SMALLINT  NULL ,
	altee                SMALLINT  NULL ,
	aproptn_cde          SMALLINT  NULL ,
	maj_cls              SMALLINT  NULL ,
	obj_clsfctn_cde      SMALLINT  NULL ,
	ppb_cde_1st          SMALLINT  NULL ,
	ppb_cde_2_3          SMALLINT  NULL ,
	sbmsn_cde            SMALLINT  NULL ,
	purp_cde             SMALLINT  NULL ,
	nbr_lns_adjd         INTEGER  NULL ,
	vou_adjmt_amt        NUMERIC(11,2)  NULL ,
	oblgn_ttl_amt        NUMERIC(11,2)  NULL ,
	altmt                NUMERIC(12,2)  NULL ,
	grp_of_altmt_cde     CHAR(3)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.altmadj_new
( 
	agcy                 CHAR(2)  NULL ,
	vou_nbr              INTEGER  NULL ,
	vou_yr               SMALLINT  NULL ,
	vou_mo               SMALLINT  NULL ,
	vou_day              SMALLINT  NULL ,
	trnsctn_cde_updte    CHAR(2)  NULL ,
	blk_nbr              SMALLINT  NULL ,
	dte_blk_proc_ctry    NUMERIC(8)  NULL ,
	stat_cde             SMALLINT  NULL ,
	prepr_init           VARCHAR(4) NULL ,
	addtnl_rmrks         VARCHAR(48)  NULL ,
	adjmt_user_id        VARCHAR(6)  NULL ,
	nbr_of_occurs        SMALLINT  NULL ,
	fy                   SMALLINT  NULL ,
	altee                SMALLINT  NULL ,
	aproptn_cde_expnd    SMALLINT  NULL ,
	grp_of_altmt_cde     CHAR(3)  NULL ,
	maj_cls_expnd        SMALLINT  NULL ,
	obj_clsfctn_cde      SMALLINT  NULL ,
	ppb_cde_1st          SMALLINT  NULL ,
	ppb_cde_2_3          SMALLINT  NULL ,
	sbmsn_cde            SMALLINT  NULL ,
	purp_cde             SMALLINT  NULL ,
	nbr_lns_adjd         INTEGER  NULL ,
	vou_amt_adjmt        NUMERIC(14,2)  NULL ,
	oblgn_amt_adjmt      NUMERIC(14,2)  NULL ,
	altmt_amt_adjmt      NUMERIC(14,2)  NULL ,
	updte_cde_gl         CHAR(1)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.altmt
( 
	aproptn_cde          SMALLINT  NULL ,
	maj_cls              SMALLINT  NULL ,
	obj_clsfctn_cde      SMALLINT  NULL  
);

CREATE TABLE IF NOT EXISTS farms.amortd_cst
( 
	dte_of_chg_lst_pymt  INTEGER  NULL ,
	prin_unpd_each_chg   NUMERIC(7,2)  NULL ,
	recvrbl_cst_mtly_instlmt NUMERIC(7,2)  NULL ,
	mo_yr_1st_instlmt    SMALLINT  NULL ,
	instlmts_pd_cnt      SMALLINT  NULL ,
	amortn_prd_amortd_cst SMALLINT  NULL  
);

CREATE TABLE IF NOT EXISTS farms.aproptn_lookup
( 
	aproptn_cde          SMALLINT  NULL ,
	maj_cls              SMALLINT  NULL ,
	ppb_cde_1st          SMALLINT  NULL ,
	ppb_cde_2_3          SMALLINT  NULL ,
	aproptn_sym          VARCHAR(14)  NULL ,
	aproptn_title        VARCHAR(54)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.assistance
( 
	int_asstnc_cum_amt   NUMERIC(9,2)  NULL ,
	yr_int_asstnc_agrmt_exprtn SMALLINT  NULL ,
	mo_int_asstnc_agrmt_exprtn SMALLINT  NULL ,
	int_asstnc_recptr_cde SMALLINT  NULL ,
	int_asstnc_instlmt_next_amt NUMERIC(7,2)  NULL ,
	yr_next_int_asstnc_instlmt SMALLINT  NULL ,
	yr_instlmt_due_save  SMALLINT  NULL ,
	instlmt_due_amt_save NUMERIC(8,2)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.assoc_prin_bond
( 
	bond_cde             SMALLINT  NULL ,
	int_unpd_due_bond_accts NUMERIC(9,2)  NULL ,
	prin_unpd_due_bond_accts NUMERIC(9,2)  NULL ,
	int_next_instlmt_bond_accts NUMERIC(9,2)  NULL ,
	prin_next_instlmt_bond_accts NUMERIC(9,2)  NULL ,
	int_on_delq_prin     NUMERIC(9,2)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.case
( 
	case_id				 VARCHAR(15) not null primary key,
	st_cde_oblr          CHAR(2)  not NULL ,
	cty_cde_oblr         CHAR(3)  not NULL ,
	id_nbr_oblr          VARCHAR(10)  not null
);

CREATE TABLE IF NOT EXISTS farms.cdejunc
( 
	fd_cde_2             SMALLINT  NULL ,
	kind_cde_borr        SMALLINT  NULL  
);

CREATE TABLE IF NOT EXISTS farms.cdestr
( 
	src_fds_cde          SMALLINT  NULL ,
	asstnc_typ_cde       SMALLINT  NULL ,
	aproptn_cde          SMALLINT  NULL ,
	maj_cls              SMALLINT  NULL ,
	obj_clsfctn_cde      SMALLINT  NULL ,
	ppb_cde_1st          SMALLINT  NULL ,
	ppb_cde_2_3          SMALLINT  NULL ,
	typ_purp_cde         SMALLINT  NULL ,
	purp_cde             SMALLINT  NULL ,
	sbsy_aproptn_cde     SMALLINT  NULL ,
	sbsy_prog_plang_bdgtg_cde SMALLINT  NULL ,
	cr_rfm_obj_cls_cde   SMALLINT  NULL ,
	bdwn_int_asstnc_aproptn SMALLINT  NULL ,
	bdwn_int_asstnc_maj_cls SMALLINT  NULL ,
	bdwn_int_asstnc_obj_cls SMALLINT  NULL ,
	bdwn_int_asstnc_ppb  SMALLINT  NULL ,
	fincg_sbsy_aproptn_cde SMALLINT  NULL ,
	neg_sbsy_purp_cde    SMALLINT  NULL ,
	neg_sbsy_obj_cls     SMALLINT  NULL  
);

CREATE TABLE IF NOT EXISTS farms.checks
( 
	ck_stat_cde          SMALLINT  NULL ,
	advnc_multi_amt      NUMERIC(10,2)  NULL ,
	dte_ck               INTEGER  NULL ,
	assoc_advnc_clsg_cde SMALLINT  NULL ,
	dte_ck_sort          INTEGER  NULL ,
	sbsy_amt_disbrsed    NUMERIC(10,2)  NULL ,
	ctry_digit           SMALLINT  NULL ,
	eft_stat_cde         SMALLINT  NULL  
);

CREATE TABLE IF NOT EXISTS farms.ck_cntrl
( 
	rcrd_typ             SMALLINT  NULL ,
	ck_iss_ttl           NUMERIC(12,2)  NULL ,
	frads_ck_ttl         INTEGER  NULL ,
	cr_rept_fee_ttl      INTEGER  NULL ,
	rentl_asstnc_ln_ck_ttl NUMERIC(12,2)  NULL ,
	dly_ln_ck_ttl        NUMERIC(12,2)  NULL ,
	refund_ck_ttl        NUMERIC(12,2)  NULL ,
	frads_ln_ck_ttl      NUMERIC(12,2)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.ck_info
( 
	rcrd_typ             SMALLINT  NULL ,
	fd_cde_2             SMALLINT  NULL ,
	nme_flds_borr_cnt    SMALLINT  NULL ,
	mailg_lvl            CHAR(1)  NULL ,
	st_ofc_mailg         SMALLINT  NULL ,
	dst_ofc_mailg        SMALLINT  NULL ,
	st_cde_oblr          SMALLINT  NULL ,
	cty_cde_oblr         SMALLINT  NULL ,
	id_nbr_oblr          NUMERIC(10)  NULL ,
	ln_nbr               SMALLINT  NULL ,
	cr_rept_fee_cde      SMALLINT  NULL ,
	nme_oblr             VARCHAR(19)  NULL ,
	advnc_multi_amt      NUMERIC(10,2)  NULL ,
	dte_ck               INTEGER  NULL ,
	aproptn_cde          SMALLINT  NULL ,
	geog_st_cde          SMALLINT  NULL ,
	fy                   SMALLINT  NULL  
);

CREATE TABLE IF NOT EXISTS farms.ck_info_frads
( 
	rcrd_typ             SMALLINT  NULL ,
	fd_cde_2             SMALLINT  NULL ,
	st_ofc_mailg         SMALLINT  NULL ,
	dst_ofc_mailg        SMALLINT  NULL ,
	st_cde_oblr          SMALLINT  NULL ,
	cty_cde_oblr         SMALLINT  NULL ,
	id_nbr_oblr          NUMERIC(10)  NULL ,
	ln_nbr               SMALLINT  NULL ,
	cr_rept_fee_cde      SMALLINT  NULL ,
	nme_oblr             VARCHAR(19)  NULL ,
	advnc_multi_amt      NUMERIC(10,2)  NULL ,
	dte_ck               INTEGER  NULL ,
	aproptn_cde          SMALLINT  NULL ,
	geog_st_cde          SMALLINT  NULL ,
	fy                   SMALLINT  NULL ,
	fed_resv_route_nbr   NUMERIC(8)  NULL ,
	ck_digit_route_nbr   SMALLINT  NULL ,
	typ_bank_acct        CHAR(1)  NULL ,
	dpstr_acct_nbr       VARCHAR(17)  NULL ,
	enty_cde             SMALLINT  NULL ,
	ck_cncltn_cde        SMALLINT  NULL ,
	fnl_advnc_cde        SMALLINT  NULL ,
	dte_lst_rgstr_dtl    INTEGER  NULL ,
	blk_nbr              SMALLINT  NULL  
);

CREATE TABLE IF NOT EXISTS farms.client
( 
	id_nbr_oblr			 varchar(10) not null,
	nme_oblr_key         VARCHAR(20)  NULL ,	
	mailg_lvl_client     CHAR(1)  NULL ,
	mailg_lvl_fsa        CHAR(1)  NULL ,
	st_cty_oblr          INTEGER  NULL ,
	st_ofc_mailg_client  SMALLINT  NULL ,
	dst_ofc_mailg_client SMALLINT  NULL ,
	nme_flds_borr_cnt    SMALLINT  NULL ,
	adrs_flds_borr_cnt   SMALLINT  NULL ,
	nme_adrs_oblr_3      VARCHAR(19)  NULL ,
	nme_adrs_oblr_4      VARCHAR(19)  NULL ,
	zip_cde              INTEGER  NULL ,
	race_desc_cde        SMALLINT  NULL ,
	sex_cde              SMALLINT  NULL ,
	mrtl_stat            SMALLINT  NULL ,
	tax_exempt_cde       SMALLINT  NULL ,
	vet_cde              SMALLINT  NULL ,
	due_day_pymt         SMALLINT  NULL ,
	applt_typ_cde        SMALLINT  NULL ,
	net_worth_amt        NUMERIC(8)  NULL ,
	ln_nbr_lst_asgd      SMALLINT  NULL ,
	rcrd_ln_cnt          SMALLINT  NULL ,
	ln_cnt_ee            SMALLINT  NULL ,
	ln_cnt_otc           SMALLINT  NULL ,
	ln_cnt_insrd_fo      SMALLINT  NULL ,
	ln_cnt_dir_fo        SMALLINT  NULL ,
	ln_cnt_insrd_sw      SMALLINT  NULL ,
	ln_cnt_dir_sw        SMALLINT  NULL ,
	ln_cnt_insrd_rh      SMALLINT  NULL ,
	ln_cnt_dir_rh        SMALLINT  NULL ,
	ln_cnt_invstr        SMALLINT  NULL ,
	ln_cnt_assoc         SMALLINT  NULL ,
	susp_cde_acct        SMALLINT  NULL ,
	dte_lst_rgstr_acct   INTEGER  NULL ,
	rgstr_typ_lst_trnsctn SMALLINT  NULL ,
	sis_trf_cde          CHAR(1)  NULL ,
	empl_reltnshp_cde    CHAR(1)  NULL ,
	lrtf_srvcg_cde       SMALLINT  NULL ,
	
	st_ofc_mailg_fsa     SMALLINT  NULL ,
	dst_ofc_mailg_fsa    SMALLINT  NULL ,
	orgztn_cde           CHAR(1)  NULL ,
	dte_oac_estbd        INTEGER  NULL ,
	dte_oac_rslvd        INTEGER  NULL ,
	dte_oac_mrtm_efctv   INTEGER  NULL ,
	prevl_indctr         CHAR(1)  NULL ,
	nbr_complnts         SMALLINT  NULL  
);

CREATE TABLE IF NOT EXISTS farms.client_sfsi
( 
	fp_clsfctn_cde       SMALLINT  NULL ,
	fp_est_loss_amt      NUMERIC(8)  NULL ,
	fp_dte_lst_clsfd     INTEGER  NULL ,
	rh_clsfctn_cde       SMALLINT  NULL ,
	rh_est_loss_amt      NUMERIC(8)  NULL ,
	rh_dte_lst_clsfd     INTEGER  NULL ,
	rh_scrty_cde         CHAR(1)  NULL ,
	rh_scrty_vlu         NUMERIC(8)  NULL ,
	sis_trf_dte          INTEGER  NULL ,
	sis_trf_actn_cde     CHAR(1)  NULL ,
	trng_cde             CHAR(1)  NULL ,
	dte_trng_efctv       INTEGER  NULL ,
	dte_trng_exprtn      INTEGER  NULL ,
	dte_trng_compltn     INTEGER  NULL ,
	dte_trng_cde_procd   INTEGER  NULL ,
	client_fill          VARCHAR(34)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.cohort
( 
	cohort_cde           SMALLINT  NULL  
);

CREATE TABLE IF NOT EXISTS farms.crbur
( 
	cr_bur_stat_cde      CHAR(2)  NULL ,
	dte_lst_reptd        INTEGER  NULL ,
	pr_cr_bur_stat_cde   CHAR(2)  NULL ,
	lst_dte_pr_stat_cde_reptd INTEGER  NULL ,
	dte_init_rept        INTEGER  NULL ,
	dte_past_due_lst     INTEGER  NULL ,
	dte_lst_rgstr        INTEGER  NULL ,
	dte_lst_pymt         INTEGER  NULL ,
	amt_past_due_cb      NUMERIC(9,2)  NULL ,
	unpd_prin_amt_cb     NUMERIC(9,2)  NULL ,
	unpd_int_amt_cb      NUMERIC(9,2)  NULL ,
	stop_cde             SMALLINT  NULL ,
	dte_lst_stop_estbd   INTEGER  NULL ,
	nbr_stops_estbd      SMALLINT  NULL ,
	nbr_of_60_day_notcs_sent SMALLINT  NULL ,
	dte_60_day_notc_sent INTEGER  NULL ,
	adrs_chng_cde        SMALLINT  NULL ,
	cr_bur_trnsctn_typ   SMALLINT  NULL ,
	specl_cmmts_cde      CHAR(1)  NULL ,
	lgth_of_ln           SMALLINT  NULL ,
	dte_of_dspt          INTEGER  NULL ,
	nbr_of_dspts         SMALLINT  NULL ,
	dte_dspt_rslvd       INTEGER  NULL ,
	assoc_cde            CHAR(1)  NULL ,
	dltn_cde             SMALLINT  NULL ,
	dte_dltd             INTEGER  NULL ,
	nbr_times_dltd       SMALLINT  NULL ,
	ln_amt               NUMERIC(9,2)  NULL ,
	dte_clsg             INTEGER  NULL ,
	crdt_mturty_dte      INTEGER  NULL ,
	crdt_pymt_freq       CHAR(1)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.crclaims
( 
	crc_clm_nbr          VARCHAR(6)  NULL ,
	id_nbr_oblr          NUMERIC(10)  NULL ,
	nme_oblr             VARCHAR(19)  NULL ,
	nme_adrs_oblr_1      VARCHAR(19)  NULL ,
	nme_adrs_oblr_2      VARCHAR(19)  NULL ,
	city_nme             VARCHAR(25)  NULL ,
	st_abbr_1st          CHAR(1)  NULL ,
	st_abbr_2nd          CHAR(1)  NULL ,
	zip_cde              INTEGER  NULL ,
	zip_cde_lst_4        SMALLINT  NULL ,
	race_desc_cde        SMALLINT  NULL ,
	dte_crc_adjdctr_decsn INTEGER  NULL ,
	dte_crc_rcvd_ogc     INTEGER  NULL ,
	dte_crc_rcvd_flp     INTEGER  NULL ,
	crc_wrtf_indctr      CHAR(1)  NULL ,
	dte_crc_fo_ln_prrty_rqstd INTEGER  NULL ,
	crc_fo_ln_rqstd_st_cty INTEGER  NULL ,
	dte_crc_fo_ln_sbmtd  INTEGER  NULL ,
	dte_crc_fo_ln_apprvd INTEGER  NULL ,
	dte_crc_fo_ln_denied INTEGER  NULL ,
	crc_fo_appeal_indctr CHAR(1)  NULL ,
	dte_crc_fo_ln_clsg   INTEGER  NULL ,
	crc_fo_ln_amt        NUMERIC(11,2)  NULL ,
	dte_crc_ol_ln_prrty_rqstd INTEGER  NULL ,
	crc_ol_ln_rqstd_st_cty INTEGER  NULL ,
	dte_crc_ol_ln_sbmtd  INTEGER  NULL ,
	dte_crc_ol_ln_apprvd INTEGER  NULL ,
	dte_crc_ol_ln_denied INTEGER  NULL ,
	crc_ol_appeal_indctr CHAR(1)  NULL ,
	dte_crc_ol_ln_clsg   INTEGER  NULL ,
	crc_ol_ln_amt        NUMERIC(11,2)  NULL ,
	dte_crc_lse_purch_rqstd INTEGER  NULL ,
	crc_lse_purch_st_cty INTEGER  NULL ,
	dte_crc_lse_purch_sbmtd INTEGER  NULL ,
	dte_crc_lse_purch_apprvd INTEGER  NULL ,
	dte_crc_lse_purch_denied INTEGER  NULL ,
	crc_lse_purch_indctr CHAR(1)  NULL ,
	dte_crc_lse_purch_clsg INTEGER  NULL ,
	crc_lse_purch_amt    NUMERIC(11,2)  NULL ,
	wrtf_cum_amt         NUMERIC(13,2)  NULL ,
	dte_lst_updte        INTEGER  NULL ,
	authy_cde_trml_oprtr CHAR(1)  NULL ,
	prfcy_lvl_trml_oprtr CHAR(1)  NULL ,
	id_trml_oprtr        CHAR(3)  NULL ,
	prrty_elgblty_cde    CHAR(1)  NULL ,
	crc_yr_dscrmtn_clmd  SMALLINT  NULL ,
	ln_typ_abbr          CHAR(2)  NULL ,
	dte_crc_prrty_ltr_procd INTEGER  NULL ,
	dte_crc_fo_appeal_decsn INTEGER  NULL ,
	dte_crc_ol_appeal_decsn INTEGER  NULL ,
	dte_crc_lse_appeal_decsn INTEGER  NULL  
);

CREATE TABLE IF NOT EXISTS farms.crrate
( 
	cr_rfm_yr            SMALLINT  NULL ,
	cr_rfm_mo            SMALLINT  NULL ,
	cr_rfm_day           SMALLINT  NULL ,
	cr_rfm_rate          NUMERIC(6,6)  NULL ,
	rcrd_typ_cde         CHAR(1)  NULL ,
	ctry_digit           SMALLINT  NULL  
);

CREATE TABLE IF NOT EXISTS farms.cty_lookup
( 
	st_cde_fmha          SMALLINT  NULL ,
	cty_cde_fmha         SMALLINT  NULL ,
	cty_ofc_mailg        INTEGER  NULL ,
	srvcg_ofc_cde_cty    INTEGER  NULL ,
	fips_st_cde          SMALLINT  NULL ,
	fips_cty_cde         SMALLINT  NULL ,
	dst_srvcg_cde        SMALLINT  NULL ,
	dst_ofc_mailg        SMALLINT  NULL ,
	nme_cty              VARCHAR(20)  NULL ,
	hq_twn               VARCHAR(20)  NULL ,
	st_abbr              CHAR(2)  NULL ,
	orgztn_struc         SMALLINT  NULL ,
	cong_dst_cde_cty     NUMERIC(9)  NULL ,
	adrs_mailg_cty_ofc   CHAR(36)  NULL ,
	zip_cde_cty_ofc      INTEGER  NULL  
);

CREATE TABLE IF NOT EXISTS farms.dallot
( 
	distrbn_ttl_1st_acctg_prd NUMERIC(12,2)  NULL ,
	distrbn_ttl_2nd_acctg_prd NUMERIC(12,2)  NULL ,
	distrbn_ttl_3rd_acctg_prd NUMERIC(12,2)  NULL ,
	distrbn_ttl_4th_acctg_prd NUMERIC(12,2)  NULL ,
	oblgns_amt_cum       NUMERIC(12,2)  NULL ,
	oblgns_cnt_cum       INTEGER  NULL ,
	vou_amt              NUMERIC(12,2)  NULL ,
	fy_acctg             SMALLINT  NULL  
);

CREATE TABLE IF NOT EXISTS farms.dallot_dtl
( 
	aproptn_cde          SMALLINT  NULL ,
	maj_cls              SMALLINT  NULL ,
	obj_clsfctn_cde      SMALLINT  NULL ,
	geog_st_cde          SMALLINT  NULL ,
	lvl_cde              SMALLINT  NULL ,
	fy_acctg             SMALLINT  NULL ,
	multi_elmt_cde       SMALLINT  NULL ,
	ok_to_proc_cde       SMALLINT  NULL ,
	distrbn_cur          NUMERIC(12,2)  NULL ,
	distrbn_typ_cde      SMALLINT  NULL ,
	prd_cde              SMALLINT  NULL ,
	distrbn_st_1st_acctg_prd NUMERIC(12,2)  NULL ,
	distrbn_st_2nd_acctg_prd NUMERIC(12,2)  NULL ,
	distrbn_st_3rd_acctg_prd NUMERIC(12,2)  NULL ,
	distrbn_st_4th_acctg_prd NUMERIC(12,2)  NULL ,
	distrbn_sbszd_rh_new NUMERIC(12,2)  NULL ,
	distrbn_sbszd_rh_old NUMERIC(12,2)  NULL ,
	distrbn_sbszd_rrh    NUMERIC(12,2)  NULL ,
	distrbn_unsbszd_hsg  NUMERIC(12,2)  NULL ,
	distrbn_insrd_ol     NUMERIC(12,2)  NULL ,
	distrbn_guar_ol      NUMERIC(12,2)  NULL ,
	distrbn_lmtd_resrcs_ol NUMERIC(12,2)  NULL ,
	distrbn_insrd_fo     NUMERIC(12,2)  NULL ,
	distrbn_guar_fo      NUMERIC(12,2)  NULL ,
	distrbn_lmtd_resrcs_fo NUMERIC(12,2)  NULL ,
	distrbn_amt          NUMERIC(12,2)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.dallot_oblgn
( 
	ppb_cde_1st          SMALLINT  NULL ,
	ppb_cde_2_3          SMALLINT  NULL ,
	sbmsn_cde            SMALLINT  NULL ,
	purp_cde             SMALLINT  NULL ,
	oblgns_amt_cum       NUMERIC(12,2)  NULL ,
	oblgns_cnt_cum       INTEGER  NULL ,
	vou_amt              NUMERIC(12,2)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.dallot_oth
(  
	id int not null
);

CREATE TABLE IF NOT EXISTS farms.daproc
( 
	rcrd_typ             SMALLINT  NULL ,
	rgstr_typ_cde        SMALLINT  NULL ,
	varbl_data           CHAR(220)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.discrp
( 
	trnsctn_cde_updte    CHAR(2)  NULL ,
	st_cde_oblr          CHAR(2)  NULL ,
	cty_cde_oblr         CHAR(3)  NULL ,
	id_nbr_oblr          VARCHAR(10)  NULL ,
	trnsctn_varbl_data   CHAR(57)  NULL ,
	card_nbr             CHAR(1)  NULL ,
	card_typ             CHAR(1)  NULL ,
	blk_nbr              VARCHAR(4) NULL ,
	fd_cde_2             CHAR(2)  NULL ,
	ln_nbr               CHAR(2)  NULL ,
	mo_grgrn             CHAR(2)  NULL ,
	day_grgrn            CHAR(2)  NULL ,
	yr                   CHAR(2)  NULL ,
	discrp_cde           CHAR(2)  NULL ,
	procg_seqnc_nbr      CHAR(3)  NULL ,
	procg_seqnc_nbr_orig CHAR(3)  NULL ,
	procg_typ_cde        CHAR(1)  NULL ,
	dlt_reas_cde         CHAR(2)  NULL ,
	actn_pndg_cde        CHAR(2)  NULL ,
	authy_cde            CHAR(1)  NULL ,
	rjctd_reas           CHAR(2)  NULL ,
	user_bal_amt         NUMERIC(10,2)  NULL ,
	trnsctn_nbr_times_rjcted CHAR(3)  NULL ,
	blk_nbr_orig         VARCHAR(4) NULL ,
	mo_grgrn_1           CHAR(2)  NULL ,
	day_grgrn_1          CHAR(2)  NULL ,
	yr_1                 CHAR(2)  NULL ,
	proc_dte_orig        VARCHAR(6)  NULL ,
	proc_dte_julian_orig CHAR(5)  NULL ,
	trnsctn_seqnc_nbr    CHAR(5)  NULL ,
	authy_cde_trml_oprtr CHAR(1)  NULL ,
	prfcy_lvl_trml_oprtr CHAR(1)  NULL ,
	id_trml_oprtr        CHAR(3)  NULL ,
	jurdctn_st_cde       CHAR(2)  NULL ,
	jurdctn_unit_cde     CHAR(2)  NULL ,
	manuscript_cde       CHAR(1)  NULL ,
	sys_bal_amt          NUMERIC(10,2)  NULL ,
	pr_blk_nbr           VARCHAR(4) NULL ,
	dte_lst_actv         INTEGER  NULL  
);

CREATE TABLE IF NOT EXISTS farms.discrp_misc
( 
	jurdctn_cde_pr       VARCHAR(4) NULL ,
	brnh_cde             CHAR(1)  NULL ,
	case_nbr_old         NUMERIC(15)  NULL ,
	post_switch          SMALLINT  NULL ,
	last_procg_cde       CHAR(1)  NULL ,
	work_fil             VARCHAR(6)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.dstr_setasd
( 
	dclrd_nbr            CHAR(5)  NULL ,
	stat_cde             SMALLINT  NULL ,
	dte_efctv            INTEGER  NULL ,
	dte_instlmt_due      INTEGER  NULL ,
	cncltn_mo            SMALLINT  NULL ,
	cncltn_day           SMALLINT  NULL ,
	cncltn_yr            SMALLINT  NULL ,
	prin_amt             NUMERIC(9,2)  NULL ,
	int_amt              NUMERIC(9,2)  NULL ,
	int_fcl_ln           NUMERIC(9,2)  NULL ,
	unpd_chg_advnc_fd    NUMERIC(9,2)  NULL ,
	int_advnc_fd         NUMERIC(9,2)  NULL ,
	int_fcl_advnc_fd     NUMERIC(9,2)  NULL ,
	non_cptlzd_int_instlmt NUMERIC(9,2)  NULL ,
	dfrd_ncptlzd_int_instlmt NUMERIC(9,2)  NULL ,
	dfrd_int_instlmt     NUMERIC(8,2)  NULL ,
	prin_cr_ln           NUMERIC(9,2)  NULL ,
	int_cr_ln            NUMERIC(9,2)  NULL ,
	prin_cr_advnc_from_fd NUMERIC(9,2)  NULL ,
	int_cr_advnc_from_fd NUMERIC(9,2)  NULL ,
	non_cptlzd_int_cr_amt NUMERIC(9,2)  NULL ,
	cr_dfrd_non_cptlzd_int NUMERIC(9,2)  NULL ,
	int_cr_dfrd_ln       NUMERIC(8,2)  NULL ,
	unpd_insrnc_chg      NUMERIC(9,2)  NULL ,
	prin_cr_insrnc_chg_cum NUMERIC(7,2)  NULL ,
	dte_lst_pymt         INTEGER  NULL ,
	unapl_int            NUMERIC(9,2)  NULL ,
	unapl_non_cptlzd_int NUMERIC(9,2)  NULL ,
	unapl_dfrd_non_cptlzd_int NUMERIC(9,2)  NULL ,
	unapl_dfrd_int       NUMERIC(9,2)  NULL ,
	cncld_ttl            NUMERIC(10,2)  NULL ,
	instlmt_ttl          NUMERIC(10,2)  NULL ,
	orig_unapl_int       NUMERIC(9,2)  NULL ,
	orig_unapl_non_cptlzd_int NUMERIC(9,2)  NULL ,
	orig_unapl_dfrd_int  NUMERIC(9,2)  NULL ,
	orig_unapl_dfrd_noncap NUMERIC(9,2)  NULL ,
	dte_lst_non_csh_cr   INTEGER  NULL  
);

CREATE TABLE IF NOT EXISTS farms.dterec
( 
	efctv_dte_ctry       SMALLINT  NULL ,
	yr_grgrn             SMALLINT  NULL ,
	mo_grgrn             SMALLINT  NULL ,
	day_grgrn            SMALLINT  NULL  
);

CREATE TABLE IF NOT EXISTS farms.dtl_rate
( 
	fy_oblgn_1           SMALLINT  NULL ,
	fy_oblgn_2           SMALLINT  NULL ,
	aproptn_cde          SMALLINT  NULL ,
	maj_cls              SMALLINT  NULL ,
	st_cde               SMALLINT  NULL ,
	nbr_sbsy_lns         NUMERIC(8)  NULL ,
	fp_sbsy_avg_calc_one NUMERIC(14)  NULL ,
	fp_sbsy_avg_calc_two NUMERIC(14)  NULL ,
	sbsy_rate            NUMERIC(12,4)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.easmnt
( 
	acres_easd_crop      NUMERIC(6,1)  NULL ,
	acres_easd_pstr      NUMERIC(6,1)  NULL ,
	acres_easd_wdlnd     NUMERIC(6,1)  NULL ,
	acres_easd_oth       NUMERIC(6,1)  NULL ,
	fed_typ_easmnt       SMALLINT  NULL ,
	fed_purp_easmnt      SMALLINT  NULL ,
	fed_dte_easmnt       INTEGER  NULL ,
	fed_easmnt_apprsl_amt NUMERIC(9,2)  NULL ,
	fed_easmnt_vlu       NUMERIC(9,2)  NULL ,
	st_typ_easmnt        SMALLINT  NULL ,
	st_purp_easmnt       SMALLINT  NULL ,
	st_dte_easmnt        INTEGER  NULL ,
	st_easmnt_apprsl_amt NUMERIC(9,2)  NULL ,
	st_easmnt_vlu        NUMERIC(9,2)  NULL ,
	loc_typ_easmnt       SMALLINT  NULL ,
	loc_purp_easmnt      SMALLINT  NULL ,
	loc_dte_easmnt       INTEGER  NULL ,
	loc_easmnt_apprsl_amt NUMERIC(9,2)  NULL ,
	loc_easmnt_vlu       NUMERIC(9,2)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.eqtyrvrs
( 
	dte_trnsctn          INTEGER  NULL ,
	ln_nbr               SMALLINT  NULL ,
	ln_nbr_new           SMALLINT  NULL ,
	fd_cde_2             SMALLINT  NULL ,
	fd_cde_3rd           SMALLINT  NULL ,
	fd_cde_4th           SMALLINT  NULL ,
	amortn_amt_cum       NUMERIC(11,2)  NULL ,
	prtl_sale_ln_nbr     SMALLINT  NULL ,
	prtl_sale_amortn_amt NUMERIC(11,2)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.equity
( 
	fd_cde_2             SMALLINT  NULL ,
	fd_cde_3rd           SMALLINT  NULL ,
	fd_cde_4th           SMALLINT  NULL ,
	ln_nbr               SMALLINT  NULL ,
	typ_plan_cde         SMALLINT  NULL ,
	wrtdwn_amt_scrd_re   NUMERIC(11,2)  NULL ,
	wrtdwn_amt_not_scrd_re NUMERIC(11,2)  NULL ,
	begng_mkt_vlu        NUMERIC(11,2)  NULL ,
	endg_mkt_vlu         NUMERIC(11,2)  NULL ,
	net_recvry_vlu       NUMERIC(11,2)  NULL ,
	potl_recptr_amt      NUMERIC(11,2)  NULL ,
	rcvb_amt_due         NUMERIC(11,2)  NULL ,
	rcvb_amt_pd          NUMERIC(11,2)  NULL ,
	dte_efctv            INTEGER  NULL ,
	dte_mturty           INTEGER  NULL ,
	dte_lst_csh          INTEGER  NULL ,
	dte_fnl_pymt         INTEGER  NULL ,
	dte_lst_rgstr_dtl    INTEGER  NULL ,
	rgstr_typ_lst_trnsctn SMALLINT  NULL ,
	equity_sale_contr    SMALLINT  NULL ,
	appltn_cde           CHAR(1)  NULL ,
	fully_pd_cde         CHAR(2)  NULL ,
	fnl_rcvb_cde         SMALLINT  NULL ,
	dte_sale_prop        INTEGER  NULL ,
	dte_compld_srvcg_appltn INTEGER  NULL ,
	asstnc_typ_cde       SMALLINT  NULL ,
	dte_oblgn            INTEGER  NULL ,
	cr_appld_noncsh      NUMERIC(11,2)  NULL ,
	dte_lst_noncsh       INTEGER  NULL ,
	susp_cde             SMALLINT  NULL  
);

CREATE TABLE IF NOT EXISTS farms.fd_side
( 
	altmt                NUMERIC(12,2)  NULL ,
	altmt_1st_acctg_prd  NUMERIC(12,2)  NULL ,
	altmt_2nd_acctg_prd  NUMERIC(12,2)  NULL ,
	altmt_3rd_acctg_prd  NUMERIC(12,2)  NULL ,
	altmt_4th_acctg_prd  NUMERIC(12,2)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.fdcde
( 
	fd_cde_2             SMALLINT  NULL ,
	kind_cde_borr        SMALLINT  NULL  
);

CREATE TABLE IF NOT EXISTS farms.glborr
( 
	st_cde_oblr          SMALLINT  NULL ,
	cty_cde_oblr         SMALLINT  NULL ,
	id_nbr_oblr          NUMERIC(10)  NULL ,
	ln_nbr               SMALLINT  NULL ,
	rcvb_nbr             SMALLINT  NULL ,
	rcrd_typ             SMALLINT  NULL ,
	asstnc_typ_cde       SMALLINT  NULL ,
	abbr_ln_typ          VARCHAR(4) NULL ,
	fd_cde_2             SMALLINT  NULL ,
	fd_cde_3rd           SMALLINT  NULL ,
	fd_cde_4th           SMALLINT  NULL ,
	kind_cde_borr        SMALLINT  NULL ,
	dte_oblgn            INTEGER  NULL ,
	fy_oblgn_1           SMALLINT  NULL ,
	fy_oblgn_2           SMALLINT  NULL ,
	oblgn_ttl_amt        NUMERIC(11,2)  NULL ,
	oblgn_ln_nbr         SMALLINT  NULL ,
	aproptn_cde          SMALLINT  NULL ,
	src_fds_cde          SMALLINT  NULL ,
	fy_dstr_dclrd        SMALLINT  NULL ,
	dstr_typ_cde         SMALLINT  NULL ,
	dstr_dclrd_nbr       SMALLINT  NULL ,
	ln_orgn_cde          SMALLINT  NULL ,
	sbmsn_cde            SMALLINT  NULL ,
	guarntd_ln_amt       NUMERIC(10,2)  NULL ,
	advncs_to_dte        NUMERIC(10,2)  NULL ,
	prin_cr_guarntd_ln   NUMERIC(10,2)  NULL ,
	accrd_int_guarntd_ln NUMERIC(10,2)  NULL ,
	clsg_adjmt_amt       NUMERIC(10,2)  NULL ,
	dte_clsg             INTEGER  NULL ,
	dte_mturty           INTEGER  NULL ,
	dte_guar_begn        INTEGER  NULL ,
	dte_guar_end         INTEGER  NULL ,
	dte_fnl_advnc        INTEGER  NULL ,
	borr_int_rate        NUMERIC(6,4)  NULL ,
	lndr_int_rate        NUMERIC(6,4)  NULL ,
	varbl_int_rate_cde   SMALLINT  NULL ,
	int_bas              SMALLINT  NULL ,
	pct_loss_guar        NUMERIC(7,4)  NULL ,
	cntrc_typ_cde        SMALLINT  NULL ,
	line_of_cr_cde       SMALLINT  NULL ,
	dbt_adjmt_cde        SMALLINT  NULL ,
	id_nbr_lndr          NUMERIC(10)  NULL ,
	brnh_nbr             SMALLINT  NULL ,
	orig_id_nbr_lndr     NUMERIC(10)  NULL ,
	orig_brnh_nbr        SMALLINT  NULL ,
	guarntd_ln_stat_cde  SMALLINT  NULL ,
	guarntd_ln_susp_cde  SMALLINT  NULL ,
	ntce_guar_exprtn     SMALLINT  NULL ,
	ntce_bdwn_exprtn     SMALLINT  NULL ,
	ntce_2nd_half_fee    SMALLINT  NULL ,
	fee_purp_cde         SMALLINT  NULL ,
	fee_pd_amt           NUMERIC(8,2)  NULL ,
	fees_chgd_cum        NUMERIC(8,2)  NULL ,
	guar_fee_rate        NUMERIC(6,4)  NULL ,
	dte_dpst_fee         INTEGER  NULL ,
	pymt_stat_cde        SMALLINT  NULL ,
	past_due_prin_guarntd NUMERIC(10,2)  NULL ,
	sched_stat_amt_guarntd NUMERIC(10,2)  NULL ,
	dte_lst_stat_rept    INTEGER  NULL ,
	dte_lst_rgstr_dtl    INTEGER  NULL ,
	dte_trf_procd        INTEGER  NULL ,
	st_cde_trfor         SMALLINT  NULL ,
	cty_cde_trfor        SMALLINT  NULL ,
	id_nbr_trfor         NUMERIC(10)  NULL ,
	asumptn_agrmt_cde    SMALLINT  NULL ,
	trf_cde              SMALLINT  NULL ,
	trf_fee_guarntd      NUMERIC(10,2)  NULL ,
	dte_dpst_trf_fee     INTEGER  NULL ,
	dte_dlqcy_rept       INTEGER  NULL ,
	dlqcy_cde            SMALLINT  NULL ,
	int_asstnc_cde       SMALLINT  NULL ,
	bdwn_cde             SMALLINT  NULL ,
	bdwn_dte             INTEGER  NULL ,
	begng_cur_sbsy_prd   INTEGER  NULL ,
	end_lst_sbsy_prd     INTEGER  NULL ,
	sbsy_begng_prin      NUMERIC(10,2)  NULL ,
	prin_advnc_cur_prd   NUMERIC(10,2)  NULL ,
	prin_cr_cur          NUMERIC(10,2)  NULL ,
	sbsy_endg_prin       NUMERIC(10,2)  NULL ,
	sbsy_begng_int       NUMERIC(8,2)  NULL ,
	int_cr_cur           NUMERIC(10,2)  NULL ,
	sbsy_endg_int        NUMERIC(8,2)  NULL ,
	dte_lst_sbsy_pd      INTEGER  NULL ,
	sbsy_pd_lst_prd      NUMERIC(9,2)  NULL ,
	sbsy_pd_cum          NUMERIC(10,2)  NULL ,
	dte_int_asstnc_cncltn INTEGER  NULL ,
	cur_int_asstnc_rate  NUMERIC(6,4)  NULL ,
	pymts_cur_prd        SMALLINT  NULL ,
	dte_offset_estbd     INTEGER  NULL ,
	offset_amt           NUMERIC(10,2)  NULL ,
	offset_amt_pd        NUMERIC(10,2)  NULL ,
	offset_amt_mtly      NUMERIC(10,2)  NULL ,
	int_asstnc_recptr_due NUMERIC(10,2)  NULL ,
	int_asstnc_recptr_pd NUMERIC(10,2)  NULL ,
	dte_int_asstnc_recptr_pd INTEGER  NULL ,
	int_asstnc_trmntn_cde SMALLINT  NULL ,
	dte_anl_revw         INTEGER  NULL ,
	begng_int_asstnc_prd INTEGER  NULL ,
	end_int_asstnc_prd   INTEGER  NULL ,
	fp_begng_prin        NUMERIC(10,2)  NULL ,
	fp_amt_advnc_cur_prd NUMERIC(10,2)  NULL ,
	fp_prin_cr_cur_prd   NUMERIC(10,2)  NULL ,
	fp_endg_prin         NUMERIC(10,2)  NULL ,
	fp_begng_int         NUMERIC(8,2)  NULL ,
	fp_int_cr_cur_prd    NUMERIC(10,2)  NULL ,
	fp_endg_int          NUMERIC(8,2)  NULL ,
	dte_lst_int_asstnc_pd INTEGER  NULL ,
	dte_lst_int_asstnc_fee_pd INTEGER  NULL ,
	int_asstnc_fees_ttl  NUMERIC(8,2)  NULL ,
	cur_int_asstnc_amt   NUMERIC(9,2)  NULL ,
	int_asstnc_pd_cur_prd NUMERIC(9,2)  NULL ,
	int_asstnc_pd_lst_prd NUMERIC(9,2)  NULL ,
	int_asstnc_pd_ttl    NUMERIC(10,2)  NULL ,
	int_asstnc_term      SMALLINT  NULL ,
	fp_int_asstnc_clsg_dte INTEGER  NULL ,
	dte_lqdtn_rspnsblty  INTEGER  NULL ,
	prtctve_advncs       NUMERIC(9,2)  NULL ,
	apprsl_fee_pymt      NUMERIC(9,2)  NULL ,
	apprsl_fee_repymt    NUMERIC(9,2)  NULL ,
	dte_apprsl_fee_pymt  INTEGER  NULL ,
	dte_reorgn_end       INTEGER  NULL ,
	dte_redctn_exprtn    INTEGER  NULL ,
	orig_mkt_vlu_guarntd NUMERIC(10,2)  NULL ,
	loss_typ             CHAR(1)  NULL ,
	loss_pymt_typ        SMALLINT  NULL ,
	dte_loss_pymt        INTEGER  NULL ,
	loss_pymt_amt        NUMERIC(10,2)  NULL ,
	int_loss_pymt_amt    NUMERIC(10,2)  NULL ,
	int_earned_refund    NUMERIC(9,2)  NULL ,
	dte_recvry_loss      INTEGER  NULL ,
	recvry_loss_amt      NUMERIC(10,2)  NULL ,
	dte_recptr_pymt      INTEGER  NULL ,
	recptr_pymt_amt      NUMERIC(10,2)  NULL ,
	guar_loss_pct_pd     NUMERIC(7,4)  NULL ,
	certfd_ln            CHAR(1)  NULL ,
	lndr_int_rate_non_guarntd NUMERIC(6,4)  NULL ,
	avg_prin_bal         NUMERIC(8,2)  NULL ,
	id_nbr_hldr          NUMERIC(10)  NULL ,
	nme_hldr_1           VARCHAR(22)  NULL ,
	nme_adrs_hldr_2      VARCHAR(22)  NULL ,
	nme_adrs_hldr_3      VARCHAR(22)  NULL ,
	nme_adrs_hldr_4      VARCHAR(22)  NULL ,
	nme_adrs_hldr_5      VARCHAR(22)  NULL ,
	zip_cde_hldr         INTEGER  NULL ,
	ln_amt_purchd_by_hldr NUMERIC(10,2)  NULL ,
	dte_purchd           INTEGER  NULL ,
	purchd_reas          SMALLINT  NULL ,
	prin_pd_hldr         NUMERIC(10,2)  NULL ,
	int_pd_hldr          NUMERIC(9,2)  NULL ,
	dte_lst_int_pd_by_lndr INTEGER  NULL ,
	srvc_fee_pct         NUMERIC(6,4)  NULL ,
	prin_crs_rcvb        NUMERIC(10,2)  NULL ,
	int_crs_rcvb         NUMERIC(9,2)  NULL ,
	dte_int_pd_thru_to_fmha INTEGER  NULL ,
	lst_prin_pymt_dte    INTEGER  NULL ,
	int_accrd_to_lst_prin_dte NUMERIC(10,2)  NULL ,
	dfrd_int_crs         NUMERIC(10,2)  NULL ,
	dfrd_prin            NUMERIC(10,2)  NULL ,
	dfrd_prin_crs        NUMERIC(10,2)  NULL ,
	dfrd_int             NUMERIC(10,2)  NULL ,
	dte_dfrl_efctv       INTEGER  NULL ,
	dte_dfrl_cncltn      INTEGER  NULL ,
	dfrd_int_incm        NUMERIC(10,2)  NULL ,
	dfrd_prin_cde        CHAR(1)  NULL ,
	accrd_lost_incm      NUMERIC(10,2)  NULL ,
	dte_dfrd_prin_lst_pd INTEGER  NULL ,
	dfrd_int_rate        NUMERIC(6,4)  NULL ,
	dte_dmnd             INTEGER  NULL ,
	srvc_fee_amt         NUMERIC(10,2)  NULL ,
	srvc_fee_pd          NUMERIC(10,2)  NULL ,
	dte_prev_int_pymt    INTEGER  NULL ,
	dte_prev_prin_pymt   INTEGER  NULL ,
	dte_dfrd_int         INTEGER  NULL ,
	unearnd_sbsy         NUMERIC(8,2)  NULL ,
	dte_dmnd_fmha        INTEGER  NULL ,
	int_accrl_trmntn_cde CHAR(1)  NULL ,
	guarntd_ln_cnt_cum   INTEGER  NULL ,
	ln_amt_cum           NUMERIC(14,2)  NULL ,
	prin_cr_cum          NUMERIC(14,2)  NULL ,
	accrd_int_cum        NUMERIC(14,2)  NULL ,
	guar_fee_chgd_cum    NUMERIC(12,2)  NULL ,
	guar_fee_pd_cum      NUMERIC(12,2)  NULL ,
	guarntd_ln_sbsy_cum  NUMERIC(12,2)  NULL ,
	advncs_by_fmha_cum   NUMERIC(10,2)  NULL ,
	loss_pymt_amt_cum    NUMERIC(14,2)  NULL ,
	recptr_rcvd_cum      NUMERIC(12,2)  NULL ,
	prin_rcvb_cum        NUMERIC(12,2)  NULL ,
	int_rcvb_cum         NUMERIC(12,2)  NULL ,
	int_asstnc_pd_cum    NUMERIC(12,2)  NULL ,
	int_asstnc_fee_pd_cum NUMERIC(12,2)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.gllndr
( 
	id_nbr_lndr          NUMERIC(10)  NULL ,
	brnh_nbr             SMALLINT  NULL ,
	rcrd_typ             SMALLINT  NULL ,
	lndr_rcrd_cnt        INTEGER  NULL ,
	run_nbr_ctrl         SMALLINT  NULL ,
	dte_updte            INTEGER  NULL ,
	dte_prev_updte       INTEGER  NULL ,
	file_proc_flag       CHAR(1)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.imcase
( 
	st_cde_oblr          SMALLINT  NULL ,
	cty_cde_oblr         SMALLINT  NULL ,
	id_nbr_oblr          NUMERIC(10)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.initman
( 
	jurdctn_st_cde       CHAR(2)  NULL ,
	jurdctn_unit_cde     CHAR(2)  NULL ,
	cmmts                CHAR(78)  NULL ,
	menu_slctn_2_mfh     SMALLINT  NULL ,
	submenu_optn         SMALLINT  NULL ,
	efctv_dte_ctry       SMALLINT  NULL ,
	yr                   SMALLINT  NULL ,
	efctv_dte_mo         SMALLINT  NULL ,
	efctv_dte_day        SMALLINT  NULL ,
	ln_nbr               SMALLINT  NULL ,
	trnsctn_cntrl_amt_mfh NUMERIC(11,2)  NULL ,
	dte_viewd_ctry       SMALLINT  NULL ,
	dte_viewd_yr         SMALLINT  NULL ,
	dte_viewd_mo         SMALLINT  NULL ,
	dte_viewd_day        SMALLINT  NULL ,
	dte_lst_revw_ctry    SMALLINT  NULL ,
	dte_lst_revw_yr      SMALLINT  NULL ,
	dte_lst_revw_mo      SMALLINT  NULL ,
	dte_lst_revw_day     SMALLINT  NULL ,
	authy_cde_trml_oprtr CHAR(1)  NULL ,
	prfcy_lvl_trml_oprtr CHAR(1)  NULL ,
	id_trml_oprtr        CHAR(3)  NULL ,
	authy_cde_pr         CHAR(1)  NULL ,
	id_pr                CHAR(5)  NULL ,
	trnsctn_avlbl_indctr_mfh CHAR(1)  NULL ,
	nbr_of_occurs        SMALLINT  NULL ,
	trnsctn_elmt_fld     CHAR(1)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.insrnc_authy
( 
	ppb_cde_1st          SMALLINT  NULL ,
	ppb_cde_2_3          SMALLINT  NULL ,
	sbmsn_cde            SMALLINT  NULL ,
	purp_cde             SMALLINT  NULL ,
	altmt                NUMERIC(12,2)  NULL ,
	oblgns_amt_cum       NUMERIC(12,2)  NULL ,
	oblgns_cnt_cum       INTEGER  NULL ,
	vou_amt              NUMERIC(12,2)  NULL ,
	altmt_1st_acctg_prd  NUMERIC(12,2)  NULL ,
	altmt_2nd_acctg_prd  NUMERIC(12,2)  NULL ,
	altmt_3rd_acctg_prd  NUMERIC(12,2)  NULL ,
	altmt_4th_acctg_prd  NUMERIC(12,2)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.installment
( 
	dte_instlmt_due      INTEGER  NULL ,
	instlmt_due_amt      NUMERIC(8,2)  NULL ,
	instlmt_typ_cde      SMALLINT  NULL ,
	mturd_cde_dir_re     SMALLINT  NULL  
);

CREATE TABLE IF NOT EXISTS farms.insurance
( 
	chg_typ_cde          SMALLINT  NULL ,
	insrnc_chgs_cum_amt  NUMERIC(7,2)  NULL ,
	prin_cr_insrnc_chg_cum NUMERIC(7,2)  NULL ,
	insrnc_chg_mturd_cur_yr NUMERIC(7,2)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.int_asstnc
( 
	tax_1st_yr_cde       SMALLINT  NULL ,
	insrnc_prop          SMALLINT  NULL ,
	txs_on_prop_1st_yr_int_asstnc SMALLINT  NULL ,
	txs_on_prop_2nd_yr_int_asstnc SMALLINT  NULL ,
	int_asstnc_diff_1st_yr INTEGER  NULL ,
	int_asstnc_diff_2nd_yr INTEGER  NULL  
);

CREATE TABLE IF NOT EXISTS farms.int_bdwn
( 
	comptn_amt_bdwn      NUMERIC(10,2)  NULL ,
	int_rate_bdwn        NUMERIC(6,4)  NULL ,
	term_of_bdwn         SMALLINT  NULL ,
	oblgn_amt_bdwn       NUMERIC(10,2)  NULL ,
	oblgn_dte_bdwn       INTEGER  NULL ,
	susp_cde_bdwn        SMALLINT  NULL ,
	max_sbsy_due_bdwn    NUMERIC(10,2)  NULL ,
	dte_apprvl_bdwn      INTEGER  NULL ,
	borr_rate_bdwn       NUMERIC(6,4)  NULL ,
	fy_oblgn_occurd_bdwn SMALLINT  NULL ,
	cur_yr_int_asstnc    NUMERIC(8,2)  NULL ,
	int_asstnc_max_amt   NUMERIC(8,2)  NULL ,
	purp_cde_bdwn        SMALLINT  NULL ,
	sbmsn_cde_bdwn       SMALLINT  NULL ,
	src_fds_cde          SMALLINT  NULL  
);

CREATE TABLE IF NOT EXISTS farms.invstr_dtl
( 
	int_rate_invstr      NUMERIC(6,4)  NULL ,
	int_rate_cde         SMALLINT  NULL ,
	fd_cde_2_invstmt     SMALLINT  NULL ,
	fd_cde_3rd_invstmt   SMALLINT  NULL ,
	fd_cde_4th_invstmt   SMALLINT  NULL ,
	prin_cr_ln_cum_invstr NUMERIC(9,2)  NULL ,
	int_cr_ln_cum_invstr NUMERIC(9,2)  NULL ,
	int_fcl_ln_invstr    NUMERIC(9,2)  NULL ,
	anl_chg_rtnd         NUMERIC(9,2)  NULL ,
	int_prem_cum_amt     NUMERIC(9,2)  NULL ,
	anl_pymt_due_invstr  NUMERIC(9,2)  NULL ,
	int_unpd_ln_sale     NUMERIC(9,2)  NULL ,
	fully_pd_cde_invstmt SMALLINT  NULL ,
	dte_sale_invstr      INTEGER  NULL ,
	dte_invstr_lst_pd_invstmt INTEGER  NULL ,
	fully_pd_cde_sld_ln  SMALLINT  NULL ,
	fixd_prd_cde         CHAR(1)  NULL ,
	dte_cur_prd_agrmt_ex INTEGER  NULL ,
	fixd_prd_cur_lgth    SMALLINT  NULL ,
	yr_init_fixd_prd_exprtn SMALLINT  NULL ,
	dte_next_anl_pymt_invstr INTEGER  NULL ,
	int_asstnc_liab      INTEGER  NULL ,
	susp_cde_invstmt     SMALLINT  NULL ,
	dte_lst_rgstr_dtl_invstr INTEGER  NULL ,
	rgstr_typ_lst_chng_invstr SMALLINT  NULL ,
	ln_amt_invstr        NUMERIC(9,2)  NULL ,
	instlmt_due_invstr   NUMERIC(8,2)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.invstr_info
( 
	id_nbr_invstr        INTEGER  NULL ,
	st_cde_invstr        SMALLINT  NULL ,
	multi_acct_invstr    SMALLINT  NULL ,
	nme_invstr_1         VARCHAR(22)  NULL ,
	nme_adrs_invstr_2    VARCHAR(22)  NULL ,
	nme_adrs_invstr_3    VARCHAR(22)  NULL ,
	nme_adrs_invstr_4    VARCHAR(22)  NULL ,
	nme_adrs_invstr_5    VARCHAR(22)  NULL ,
	nme_adrs_invstr_6    CHAR(15)  NULL ,
	zip_cde_invstr       INTEGER  NULL ,
	prin_unpd_blk_sale_invstr NUMERIC(11,2)  NULL ,
	int_pymt_due_blk_sale NUMERIC(11,2)  NULL ,
	prin_redctn_invstr   NUMERIC(9,2)  NULL ,
	prin_remtnc_invstr   NUMERIC(6,2)  NULL ,
	cntrc_nbr_blk_sale   SMALLINT  NULL ,
	series_nbr           CHAR(1)  NULL ,
	int_rate_invstr_blk_sale NUMERIC(6,4)  NULL ,
	dte_invstr_lst_pd    INTEGER  NULL ,
	invstr_ttl_lns_cnt   INTEGER  NULL ,
	exch_cde_invstmt     SMALLINT  NULL ,
	natl_loc_cde_invstr  SMALLINT  NULL ,
	invstr_typ_cde       SMALLINT  NULL ,
	susp_cde_invstr_acct SMALLINT  NULL  
);

CREATE TABLE IF NOT EXISTS farms.invstr_info_misc
( 
	tax_id_typ_invstr    SMALLINT  NULL ,
	tax_id_nbr_invstr    NUMERIC(9)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.jdgmt_3rd_party
( 
	nme_flds_3rd_party_jdgmt_cnt SMALLINT  NULL ,
	adrs_flds_3rd_party_jdgmt_cnt SMALLINT  NULL ,
	nme_3rd_party_jdgmt  VARCHAR(19)  NULL ,
	nme_adrs_3rd_party_jdgmt_1 VARCHAR(19)  NULL ,
	nme_adrs_3rd_party_jdgmt_2 VARCHAR(19)  NULL ,
	nme_adrs_3rd_party_jdgmt_3 VARCHAR(19)  NULL ,
	nme_adrs_3rd_party_jdgmt_4 VARCHAR(19)  NULL ,
	zip_cde_3rd_party_jdgmt INTEGER  NULL  
);

CREATE TABLE IF NOT EXISTS farms.job_restart
( 
	prog_id              VARCHAR(8)  NULL ,
	prog_start_dte       INTEGER  NULL ,
	prog_start_time      NUMERIC(8)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.jurdctn
( 
	jurdctn_st_cde       CHAR(2)  NULL ,
	jurdctn_unit_cde     CHAR(2)  NULL ,
	jurdctn_next_key     NUMERIC(8)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.lessee
( 
	st_cde_lsee          SMALLINT  NULL ,
	cty_cde_lsee         SMALLINT  NULL ,
	id_lsee              NUMERIC(10)  NULL ,
	nme_flds_lsee_cnt    SMALLINT  NULL ,
	adrs_flds_lsee_cnt   SMALLINT  NULL ,
	nme_lsee             VARCHAR(19)  NULL ,
	nme_adrs_lsee_1      VARCHAR(19)  NULL ,
	nme_adrs_lsee_2      VARCHAR(19)  NULL ,
	nme_adrs_lsee_3      VARCHAR(19)  NULL ,
	nme_adrs_lsee_4      VARCHAR(19)  NULL ,
	zip_cde_lsee         INTEGER  NULL ,
	lsee_typ_cde         SMALLINT  NULL ,
	lsee_race_cde        SMALLINT  NULL  
);

CREATE TABLE IF NOT EXISTS farms.ln_aid
( 
	debt_set_aside_ln_amt NUMERIC(8,2)  NULL ,
	debt_set_aside_ln_cncld NUMERIC(8,2)  NULL ,
	debt_set_aside_ln_offset NUMERIC(8,2)  NULL ,
	dte_dfrl_cncltn_ln   INTEGER  NULL ,
	dte_dfrl_efctv_ln    INTEGER  NULL ,
	int_cr_dfrd_ln       NUMERIC(8,2)  NULL ,
	dfrd_int_instlmt     NUMERIC(8,2)  NULL ,
	dfrd_int_ln_amt      NUMERIC(8,2)  NULL ,
	dfrd_non_cptlzd_int_amt NUMERIC(9,2)  NULL ,
	dfrd_ncptlzd_int_instlmt NUMERIC(9,2)  NULL ,
	cr_dfrd_non_cptlzd_int NUMERIC(9,2)  NULL ,
	dfrd_prin_ln_amt     NUMERIC(9,2)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.ln_no_int
( 
	non_cptlzd_int_ln_amt NUMERIC(9,2)  NULL ,
	non_cptlzd_int_cr_amt NUMERIC(9,2)  NULL ,
	non_cptlzd_int_instlmt NUMERIC(9,2)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.lnrate
( 
	dte_efctv            INTEGER  NULL ,
	int_rate_borr        NUMERIC(6,4)  NULL ,
	non_prog_int_rate    NUMERIC(6,4)  NULL ,
	ctry_digit           SMALLINT  NULL  
);

CREATE TABLE IF NOT EXISTS farms.loan
( 
	int_rate_borr_1st    NUMERIC(6,6)  NULL ,
	appltn_cde           CHAR(1)  NULL ,
	fully_pd_cde         CHAR(2)  NULL ,
	fully_mturd_cde      SMALLINT  NULL ,
	advnc_unclsd_cde     SMALLINT  NULL ,
	act_collctn_only_cde SMALLINT  NULL ,
	assoc_typ_note_cde   SMALLINT  NULL ,
	purch_cde            CHAR(1)  NULL ,
	nbr_pymts_amortn     SMALLINT  NULL ,
	instlmts_int_only_cnt SMALLINT  NULL ,
	sale_stat_cde        SMALLINT  NULL ,
	fixd_prd_init_lgth   SMALLINT  NULL ,
	mort_hldr_cde        SMALLINT  NULL ,
	yr_ln_clsd           SMALLINT  NULL ,
	dte_ln_sld_or_pldgd  INTEGER  NULL ,
	fmha_dir_to_insrd_cde SMALLINT  NULL ,
	dte_clsg             INTEGER  NULL ,
	dte_ln_exprtn        SMALLINT  NULL ,
	ln_amt               NUMERIC(9,2)  NULL ,
	recvrbl_cst_chgs     NUMERIC(9,2)  NULL ,
	prin_cr_ln           NUMERIC(9,2)  NULL ,
	int_cr_ln            NUMERIC(9,2)  NULL ,
	int_fcl_ln           NUMERIC(9,2)  NULL ,
	sched_stat           NUMERIC(9,2)  NULL ,
	pymt_extra_amt_cum   NUMERIC(9,2)  NULL ,
	cr_non_csh_appltn_typ_cde CHAR(1)  NULL ,
	cr_non_csh_lst_amt_appld NUMERIC(9,2)  NULL ,
	dte_lst_non_csh_cr   INTEGER  NULL ,
	dte_lst_csh_cr       INTEGER  NULL ,
	dte_next_instlmt_due INTEGER  NULL ,
	instlmt_due_next_amt NUMERIC(8,2)  NULL ,
	instlmt_next_typ_cde SMALLINT  NULL ,
	dte_instlmt_due      INTEGER  NULL ,
	instlmt_due_amt      NUMERIC(8,2)  NULL ,
	instlmt_typ_cde      SMALLINT  NULL ,
	mturd_cde_dir_re     SMALLINT  NULL ,
	susp_cde_ln          SMALLINT  NULL ,
	dte_lst_rgstr_dtl    INTEGER  NULL ,
	rgstr_typ_lst_chng   SMALLINT  NULL ,
	ln_nbr_old           SMALLINT  NULL ,
	int_asstnc_cde       SMALLINT  NULL ,
	wrtf_cde             CHAR(1)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.loan_dre
( 
	civ_rhts_cde         SMALLINT  NULL ,
	fy_pldgd_gnma        SMALLINT  NULL ,
	int_dfrd_unmturd_amt_rmng NUMERIC(5,2)  NULL ,
	int_dfrd_anl_instlmt NUMERIC(5,2)  NULL ,
	int_dfrd_instlmt_mturty_yr SMALLINT  NULL  
);

CREATE TABLE IF NOT EXISTS farms.loan_otc
( 
	fy_pldgd_gnma_otc    SMALLINT  NULL ,
	civ_rhts_cde_otc     SMALLINT  NULL ,
	int_rate_varbl_cde   SMALLINT  NULL ,
	amortn_prd           SMALLINT  NULL ,
	em_multi_orig_ln_nbr SMALLINT  NULL ,
	em_cde               SMALLINT  NULL ,
	int_billd_unpd_pr_stmt NUMERIC(9,2)  NULL ,
	int_billd_unpd_otc_amt NUMERIC(9,2)  NULL ,
	prin_due_otc_amt     NUMERIC(9,2)  NULL ,
	pymt_pr_to_appltn_int NUMERIC(9,2)  NULL ,
	pymt_pr_to_appltn_prin NUMERIC(9,2)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.loan_sfsi
( 
	dte_lst_revw_yr      SMALLINT  NULL ,
	dte_lst_revw_mo      SMALLINT  NULL ,
	dte_lst_revw_day     SMALLINT  NULL ,
	cp_clsfctn_cde       SMALLINT  NULL ,
	cp_dte_lst_clsfd     INTEGER  NULL ,
	cp_est_loss_amt      NUMERIC(8)  NULL ,
	ln_fill              VARCHAR(22)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.loctn_lookup
( 
	loctn_lvl_151        CHAR(1)  NULL ,
	st_cde_fmha_151      SMALLINT  NULL ,
	dst_cde_fmha_151     SMALLINT  NULL ,
	ofc_lvl_151          CHAR(1)  NULL ,
	st_cde_srvcg_151     SMALLINT  NULL ,
	dst_cde_srvcg_151    SMALLINT  NULL ,
	mailg_lvl_151        CHAR(1)  NULL ,
	st_ofc_mailg_151     SMALLINT  NULL ,
	dst_ofc_mailg_151    SMALLINT  NULL ,
	fips_st_cde_151      SMALLINT  NULL ,
	fips_cty_cde_151     SMALLINT  NULL ,
	prim_st_cde_151      SMALLINT  NULL ,
	loctn_nme_151        VARCHAR(20)  NULL ,
	st_abbr_1st_151      CHAR(1)  NULL ,
	st_abbr_2nd_151      CHAR(1)  NULL ,
	rgn_cde_151          SMALLINT  NULL ,
	st_ofc_cntrl_cde_151 SMALLINT  NULL ,
	dst_ofc_lvl_151      CHAR(1)  NULL ,
	st_cde_dst_151       SMALLINT  NULL ,
	dst_srvcg_cde_1st_151 SMALLINT  NULL ,
	dst_srvcg_cde_151    SMALLINT  NULL ,
	cong_dst_cde_cty_151 SMALLINT  NULL ,
	orgztn_struc_cty_151 INTEGER  NULL ,
	dte_updted_151       INTEGER  NULL ,
	updte_slctn_cde_151  CHAR(1)  NULL ,
	sis_ofc_lvl_151      CHAR(1)  NULL ,
	st_cde_sis_151       SMALLINT  NULL ,
	sis_srvcg_cde_1st_151 SMALLINT  NULL ,
	sis_srvcg_cde_151    SMALLINT  NULL ,
	mailg_lvl_amas_151   CHAR(1)  NULL ,
	st_ofc_mailg_amas_151 SMALLINT  NULL ,
	cty_ofc_mailg_amas_151 SMALLINT  NULL  
);

CREATE TABLE IF NOT EXISTS farms.lse_info
( 
	lse_nbr              SMALLINT  NULL ,
	fd_cde_2_lse         SMALLINT  NULL ,
	fd_cde_3rd_lse       SMALLINT  NULL ,
	fd_cde_4th_lse       SMALLINT  NULL ,
	lse_typ_cde          SMALLINT  NULL ,
	dte_lse_efctv        INTEGER  NULL ,
	dte_lse_ends         INTEGER  NULL ,
	lse_ttl_amt          NUMERIC(10,2)  NULL ,
	incm_lse             NUMERIC(10,2)  NULL ,
	dte_lst_csh_cr_lse   INTEGER  NULL ,
	stat_cde_lse         SMALLINT  NULL ,
	lse_cncld_amt        NUMERIC(10,2)  NULL ,
	wrtf_lse_amt         NUMERIC(10,2)  NULL ,
	susp_cde_lse         SMALLINT  NULL ,
	dte_lst_rgstr_dtl_lse INTEGER  NULL ,
	rgstr_typ_lst_chng_lse SMALLINT  NULL ,
	lsee_kind_cde        SMALLINT  NULL ,
	lsee_reltnshp_cde    SMALLINT  NULL ,
	instlmt_due_amt_lse_1 NUMERIC(8,2)  NULL ,
	dte_instlmt_due_lse_1 INTEGER  NULL ,
	instlmt_due_amt_lse_2 NUMERIC(8,2)  NULL ,
	dte_instlmt_due_lse_2 INTEGER  NULL ,
	instlmt_due_amt_lse_3 NUMERIC(8,2)  NULL ,
	dte_instlmt_due_lse_3 INTEGER  NULL ,
	instlmt_due_amt_lse_4 NUMERIC(8,2)  NULL ,
	dte_instlmt_due_lse_4 INTEGER  NULL ,
	instlmt_due_amt_lse_5 NUMERIC(8,2)  NULL ,
	dte_instlmt_due_lse_5 INTEGER  NULL ,
	lse_terms_amt        NUMERIC(7,2)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.mallot
( 
	aproptn_cde          SMALLINT  NULL ,
	maj_cls              SMALLINT  NULL ,
	obj_clsfctn_cde      SMALLINT  NULL ,
	fy_acctg             SMALLINT  NULL ,
	acct_typ_cde         SMALLINT  NULL ,
	multi_elmt_cde       SMALLINT  NULL ,
	ok_to_proc_cde       SMALLINT  NULL ,
	aprtnmts_cur_dtl     NUMERIC(12,2)  NULL ,
	altmt_cur            NUMERIC(12,2)  NULL ,
	aprtnmt_typ          SMALLINT  NULL ,
	altmt_typ            SMALLINT  NULL ,
	prd_cde              SMALLINT  NULL ,
	aprtnmts_1st_acctg_prd NUMERIC(12,2)  NULL ,
	aprtnmts_2nd_acctg_prd NUMERIC(12,2)  NULL ,
	aprtnmts_3rd_acctg_prd NUMERIC(12,2)  NULL ,
	aprtnmts_4th_acctg_prd NUMERIC(12,2)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.mallot_oblgn
( 
	sbmsn_cde            SMALLINT  NULL ,
	purp_cde             SMALLINT  NULL ,
	oblgns_amt_cum       NUMERIC(12,2)  NULL ,
	oblgns_cnt_cum       INTEGER  NULL ,
	vou_amt              NUMERIC(12,2)  NULL ,
	ppb_cde_1st          SMALLINT  NULL ,
	ppb_cde_2_3          SMALLINT  NULL  
);

CREATE TABLE IF NOT EXISTS farms.mallot_oth
(  
	id int not null
);

CREATE TABLE IF NOT EXISTS farms.mstr_rate
( 
	fy_oblgn_1           SMALLINT  NULL ,
	fy_oblgn_2           SMALLINT  NULL ,
	aproptn_cde          SMALLINT  NULL ,
	maj_cls              SMALLINT  NULL ,
	nbr_sbsy_lns         NUMERIC(8)  NULL ,
	fp_sbsy_avg_calc_one NUMERIC(14)  NULL ,
	fp_sbsy_avg_calc_two NUMERIC(14)  NULL ,
	sbsy_rate            NUMERIC(12,4)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.notify
( 
	rcrd_typ             SMALLINT  NULL ,
	st_cde_invstr        SMALLINT  NULL ,
	id_nbr_invstr        INTEGER  NULL ,
	st_cde_oblr          SMALLINT  NULL ,
	cty_cde_oblr         SMALLINT  NULL ,
	id_nbr_oblr          NUMERIC(10)  NULL ,
	ln_nbr               SMALLINT  NULL ,
	nme_oblr             VARCHAR(19)  NULL ,
	trnsctn_cde_updte    CHAR(2)  NULL ,
	fd_cde_2             SMALLINT  NULL ,
	fd_cde_3rd           SMALLINT  NULL ,
	fd_cde_4th           SMALLINT  NULL ,
	int_rate_invstr      NUMERIC(6,4)  NULL ,
	int_rate_borr        NUMERIC(6,4)  NULL ,
	pymt_cde_invstr      SMALLINT  NULL ,
	anl_chg_rtnd         NUMERIC(9,2)  NULL ,
	int_pd_invstr        NUMERIC(9,2)  NULL ,
	prin_pd_invstr       NUMERIC(9,2)  NULL ,
	prin_unpd_invstr     NUMERIC(9,2)  NULL ,
	fed_resv_cde         SMALLINT  NULL ,
	fixd_prd_cde         CHAR(1)  NULL ,
	dte_cur_prd_agrmt_ex INTEGER  NULL ,
	dte_ck               INTEGER  NULL ,
	mort_hldr_cde        SMALLINT  NULL ,
	note_appld_amt       NUMERIC(9,2)  NULL ,
	dte_efctv            INTEGER  NULL ,
	dte_clsg             INTEGER  NULL ,
	fully_pd_cde_invstmt SMALLINT  NULL ,
	blk_nbr              SMALLINT  NULL  
);

CREATE TABLE IF NOT EXISTS farms.notify_cntrl
( 
	rcrd_typ             SMALLINT  NULL ,
	pymt_amt_ttl         NUMERIC(12,2)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.oblgn
( 
	rcrd_typ             SMALLINT  NULL ,
	adrs_card_cde        SMALLINT  NULL ,
	int_asstnc_agrmt_form_compl SMALLINT  NULL ,
	sale_cr_asumptn_cde  SMALLINT  NULL ,
	fy_oblgn_1           SMALLINT  NULL ,
	fy_oblgn_2           SMALLINT  NULL ,
	aproptn_cde          SMALLINT  NULL ,
	maj_cls              SMALLINT  NULL ,
	srvcg_ofc_cde_st     SMALLINT  NULL ,
	sbmsn_cde            SMALLINT  NULL ,
	purp_cde             SMALLINT  NULL ,
	oblgn_to_borr_ttl_amt NUMERIC(10,2)  NULL ,
	dte_oblgn            INTEGER  NULL ,
	vou_unclsd_amt       NUMERIC(10,2)  NULL ,
	ln_cnt_cde           SMALLINT  NULL ,
	fee_cr_rept_cde      SMALLINT  NULL ,
	asstnc_repair_rehbltn SMALLINT  NULL ,
	incm_fam_adjd        INTEGER  NULL ,
	dwl_typ_cde          SMALLINT  NULL ,
	vou_nbr              INTEGER  NULL ,
	guar_ln_face_vlu_amt NUMERIC(10,2)  NULL ,
	advnc_multi_ttl_amt  NUMERIC(10,2)  NULL ,
	int_cptlzd_cde       SMALLINT  NULL ,
	repymt_prd           SMALLINT  NULL ,
	ppb_cde_1st          SMALLINT  NULL ,
	ppb_cde_2_3          SMALLINT  NULL ,
	split_cmbn_rcrd_assoc_cde SMALLINT  NULL ,
	incm_ctgry_cde       SMALLINT  NULL ,
	fee_inspctn_cde      SMALLINT  NULL ,
	dte_apprvl_ln_grt    INTEGER  NULL ,
	drght_cde            SMALLINT  NULL ,
	guar_loss_pct        SMALLINT  NULL ,
	susp_cde_oblgn       SMALLINT  NULL ,
	src_fds_cde          SMALLINT  NULL ,
	init_int_asstnc_rate NUMERIC(6,4)  NULL ,
	high_cst_area        CHAR(1)  NULL ,
	amt_insrd_debt_refin NUMERIC(10,2)  NULL ,
	borr_hist_cde        SMALLINT  NULL ,
	dte_lst_rgstr_dtl_oblgn INTEGER  NULL ,
	rgstr_typ_lst_chng_oblgn SMALLINT  NULL ,
	sbsy_amt_oblgn       NUMERIC(10,2)  NULL ,
	sbsy_aproptn_cde     SMALLINT  NULL ,
	sbsy_prog_plang_bdgtg_cde SMALLINT  NULL  
);

CREATE TABLE IF NOT EXISTS farms.orders
( 
	st_cde_oblr          CHAR(2)  NULL ,
	cty_cde_oblr         CHAR(3)  NULL ,
	id_nbr_oblr          VARCHAR(10)  NULL ,
	lookd_cnt            SMALLINT  NULL  
);

CREATE TABLE IF NOT EXISTS farms.orgztn_lookup
( 
	mailg_lvl_lvl2       CHAR(1)  NULL ,
	st_ofc_mailg_lvl2    SMALLINT  NULL ,
	cty_ofc_mailg_lvl2   SMALLINT  NULL ,
	mailg_lvl_lvl3       CHAR(1)  NULL ,
	st_ofc_mailg_lvl3    SMALLINT  NULL ,
	cty_ofc_mailg_lvl3   SMALLINT  NULL  
);

CREATE TABLE IF NOT EXISTS farms.ovflo
( 
	trnsctn_cde_updte    CHAR(2)  NULL ,
	st_cde_oblr          CHAR(2)  NULL ,
	cty_cde_oblr         CHAR(3)  NULL ,
	id_nbr_oblr          VARCHAR(10)  NULL ,
	trnsctn_varbl_data   CHAR(57)  NULL ,
	card_nbr             CHAR(1)  NULL ,
	card_typ             CHAR(1)  NULL ,
	blk_nbr              VARCHAR(4) NULL  
);

CREATE TABLE IF NOT EXISTS farms.pd_acct_rvrsl
( 
	trnsctn_cde_updte    CHAR(2)  NULL ,
	fd_cde_2             SMALLINT  NULL ,
	fd_cde_3rd           SMALLINT  NULL ,
	fd_cde_4th           SMALLINT  NULL ,
	kind_cde_ln          SMALLINT  NULL ,
	bond_cde             SMALLINT  NULL ,
	assoc_typ_note_cde   SMALLINT  NULL ,
	int_rate_borr_1st    NUMERIC(6,6)  NULL ,
	dte_clsg             INTEGER  NULL ,
	act_collctn_only_cde SMALLINT  NULL ,
	susp_cde_ln          SMALLINT  NULL ,
	fully_mturd_cde      SMALLINT  NULL ,
	fixd_prd_init_lgth   SMALLINT  NULL ,
	ln_amt               NUMERIC(9,2)  NULL ,
	int_asstnc_cum_amt   NUMERIC(9,2)  NULL ,
	recvrbl_cst_chgs     NUMERIC(9,2)  NULL ,
	prin_cr_ln           NUMERIC(9,2)  NULL ,
	int_cr_ln            NUMERIC(9,2)  NULL ,
	int_fcl_ln           NUMERIC(9,2)  NULL ,
	pymt_extra_amt_cum   NUMERIC(9,2)  NULL ,
	sched_stat           NUMERIC(9,2)  NULL ,
	dte_lst_rgstr_dtl    INTEGER  NULL ,
	rgstr_typ_lst_chng   SMALLINT  NULL ,
	dte_lst_non_csh_cr   INTEGER  NULL ,
	cr_non_csh_lst_amt_appld NUMERIC(9,2)  NULL ,
	cr_non_csh_appltn_typ_cde CHAR(1)  NULL ,
	appltn_cde           CHAR(1)  NULL ,
	fully_pd_cde         CHAR(2)  NULL ,
	dte_trnsctn          INTEGER  NULL ,
	mort_hldr_cde        SMALLINT  NULL ,
	to_or_from_cde       SMALLINT  NULL ,
	st_cde_oblr          SMALLINT  NULL ,
	cty_cde_oblr         SMALLINT  NULL ,
	id_nbr_oblr          NUMERIC(10)  NULL ,
	blk_nbr              SMALLINT  NULL  
);

CREATE TABLE IF NOT EXISTS farms.plerep
( 
	rgn_cde_plerep       SMALLINT  NULL ,
	morts_frm_govt_ownd_cnt NUMERIC(7)  NULL ,
	morts_frm_ownd_govt_amt NUMERIC(14,2)  NULL ,
	mort_frm_acqd_cur_qtr_cnt INTEGER  NULL ,
	morts_acqd_on_frms_amt NUMERIC(10,2)  NULL ,
	prin_incr_frm_mort_ownd NUMERIC(10,2)  NULL ,
	morts_frm_fully_pd_cnt INTEGER  NULL ,
	pymt_fnl_frm_mort_ttl_amt NUMERIC(10,2)  NULL ,
	prin_pymt_on_oth_frm_mort NUMERIC(10,2)  NULL ,
	morts_frm_acqd_frcl_cnt INTEGER  NULL ,
	morts_frm_acqd_frcl_amt NUMERIC(10,2)  NULL ,
	rh_init_lns_1_pct_cnt SMALLINT  NULL ,
	rh_init_lns_1_pct_amt NUMERIC(7)  NULL ,
	rh_init_lns_3_pct_cnt SMALLINT  NULL ,
	rh_init_lns_3_pct_amt NUMERIC(7)  NULL ,
	rh_init_lns_6_pct_cnt SMALLINT  NULL ,
	rh_init_lns_6_pct_amt NUMERIC(7)  NULL ,
	fo_init_lns_3_pct_cnt SMALLINT  NULL ,
	fo_init_lns_3_pct_amt NUMERIC(7)  NULL ,
	fo_init_lns_5_pct_cnt SMALLINT  NULL ,
	fo_init_lns_5_pct_amt NUMERIC(7)  NULL ,
	purch_re_qtr         NUMERIC(7)  NULL ,
	ln_refin_re_prtn_fo_rh NUMERIC(7)  NULL ,
	ln_refin_non_re_prtn_fo_rh NUMERIC(7)  NULL ,
	ln_fo_rh_land_bldg_prtn NUMERIC(7)  NULL ,
	fees_oth_known       NUMERIC(7)  NULL ,
	pymt_dwn_init_lns_ttl_amt NUMERIC(7)  NULL ,
	fy_pldgd_gnma_plerep SMALLINT  NULL ,
	ln_acct_cde          SMALLINT  NULL ,
	pldg_orig_amt        NUMERIC(13,2)  NULL ,
	lns_in_orig_pldg_cnt NUMERIC(8)  NULL ,
	ln_amt_addd_cum      NUMERIC(13,2)  NULL ,
	lns_addd_cum_cnt     NUMERIC(8)  NULL ,
	advnc_addtnl_cum_amt NUMERIC(13,2)  NULL ,
	lns_cncld_cum_amt    NUMERIC(13,2)  NULL ,
	lns_cncld_cum_cnt    NUMERIC(8)  NULL ,
	prin_not_fully_pd_cum NUMERIC(13,2)  NULL ,
	int_not_fully_pd_cum NUMERIC(13,2)  NULL ,
	prin_fully_pd_cum    NUMERIC(13,2)  NULL ,
	int_fully_pd_cum_amt NUMERIC(13,2)  NULL ,
	lns_fully_pd_cum_cnt NUMERIC(8)  NULL ,
	frcl_jdgmt_cum_amt   NUMERIC(13,2)  NULL ,
	frcl_jdgmt_cum_cnt   NUMERIC(8)  NULL ,
	wrtf_cum_amt         NUMERIC(13,2)  NULL ,
	wrtf_cum             NUMERIC(8)  NULL ,
	ln_amt_addd_mtd      NUMERIC(10,2)  NULL ,
	lns_addd_mtd_cnt     INTEGER  NULL ,
	advnc_addtnl_amt_mtd NUMERIC(10,2)  NULL ,
	lns_cncld_mtd_amt    NUMERIC(10,2)  NULL ,
	lns_cncld_mtd_cnt    INTEGER  NULL ,
	prin_not_fully_pd_mtd NUMERIC(10,2)  NULL ,
	int_not_fully_pd_mtd NUMERIC(10,2)  NULL ,
	prin_fully_pd_mtd    NUMERIC(10,2)  NULL ,
	int_fully_pd_mtd     NUMERIC(10,2)  NULL ,
	lns_fully_pd_mtd_cnt INTEGER  NULL ,
	prin_frcl_jdgmt_mtd  NUMERIC(10,2)  NULL ,
	lns_frcl_jdgmt_mtd   INTEGER  NULL ,
	wrtf_unpd_prin_mtd   NUMERIC(10,2)  NULL ,
	lns_wrtf_mtd_cnt     INTEGER  NULL ,
	prin_unpd_pldgd_lns  NUMERIC(13,2)  NULL ,
	lns_outstg_cnt       NUMERIC(8)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.prog_save
( 
	prog_data            CHAR(500)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.prtlsale
( 
	prtl_sale_ln_nbr     SMALLINT  NULL ,
	prtl_net_recvry_vlu  NUMERIC(11,2)  NULL ,
	prtl_begng_mkt_vlu   NUMERIC(11,2)  NULL ,
	prtl_endg_mkt_vlu    NUMERIC(11,2)  NULL ,
	prtl_rcvb_amt_due    NUMERIC(11,2)  NULL ,
	prtl_rcvb_amt_pd     NUMERIC(11,2)  NULL ,
	prtl_dte_sale_mturty INTEGER  NULL ,
	dte_lst_csh_prtl     INTEGER  NULL ,
	prtl_appltn_cde      CHAR(1)  NULL ,
	prtl_fully_pd_cde    CHAR(2)  NULL ,
	cr_appld_noncsh_prtl NUMERIC(11,2)  NULL ,
	dte_lst_noncsh_prtl  INTEGER  NULL  
);

CREATE TABLE IF NOT EXISTS farms.rda_altmt
( 
	aproptn_cde          SMALLINT  NULL ,
	maj_cls              SMALLINT  NULL ,
	obj_clsfctn_cde      SMALLINT  NULL  
);

CREATE TABLE IF NOT EXISTS farms.rda_area_dallot
( 
	fy                   SMALLINT  NULL ,
	rda_rgn_cde          SMALLINT  NULL ,
	geog_st_cde          SMALLINT  NULL ,
	rda_area_cde         SMALLINT  NULL ,
	aproptn_cde          SMALLINT  NULL ,
	maj_cls              SMALLINT  NULL ,
	obj_clsfctn_cde      SMALLINT  NULL ,
	multi_elmt_cde       SMALLINT  NULL ,
	ok_to_proc_cde       SMALLINT  NULL ,
	distrbn_cur          NUMERIC(12,2)  NULL ,
	distrbn_typ_cde      SMALLINT  NULL ,
	prd_cde              SMALLINT  NULL ,
	distrbn_st_1st_acctg_prd NUMERIC(12,2)  NULL ,
	distrbn_st_2nd_acctg_prd NUMERIC(12,2)  NULL ,
	distrbn_st_3rd_acctg_prd NUMERIC(12,2)  NULL ,
	distrbn_st_4th_acctg_prd NUMERIC(12,2)  NULL ,
	distrbn_guar         NUMERIC(12,2)  NULL ,
	distrbn_insrd        NUMERIC(12,2)  NULL ,
	distrbn_dir          NUMERIC(12,2)  NULL ,
	distrbn_grt          NUMERIC(12,2)  NULL ,
	distrbn_amt          NUMERIC(12,2)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.rda_area_oblgn
( 
	ppb_cde_1st          SMALLINT  NULL ,
	ppb_cde_2_3          SMALLINT  NULL ,
	sbmsn_cde            SMALLINT  NULL ,
	purp_cde             SMALLINT  NULL ,
	oblgns_amt_cum       NUMERIC(12,2)  NULL ,
	oblgns_cnt_cum       INTEGER  NULL ,
	vou_amt              NUMERIC(12,2)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.rda_dallot_dtl
( 
	fy                   SMALLINT  NULL ,
	rda_rgn_cde          SMALLINT  NULL ,
	geog_st_cde          SMALLINT  NULL ,
	aproptn_cde          SMALLINT  NULL ,
	maj_cls              SMALLINT  NULL ,
	obj_clsfctn_cde      SMALLINT  NULL ,
	multi_elmt_cde       SMALLINT  NULL ,
	ok_to_proc_cde       SMALLINT  NULL ,
	distrbn_cur          NUMERIC(12,2)  NULL ,
	distrbn_typ_cde      SMALLINT  NULL ,
	prd_cde              SMALLINT  NULL ,
	distrbn_st_1st_acctg_prd NUMERIC(12,2)  NULL ,
	distrbn_st_2nd_acctg_prd NUMERIC(12,2)  NULL ,
	distrbn_st_3rd_acctg_prd NUMERIC(12,2)  NULL ,
	distrbn_st_4th_acctg_prd NUMERIC(12,2)  NULL ,
	distrbn_guar         NUMERIC(12,2)  NULL ,
	distrbn_insrd        NUMERIC(12,2)  NULL ,
	distrbn_dir          NUMERIC(12,2)  NULL ,
	distrbn_grt          NUMERIC(12,2)  NULL ,
	distrbn_amt          NUMERIC(12,2)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.rda_dallot_oblgn
( 
	ppb_cde_1st          SMALLINT  NULL ,
	ppb_cde_2_3          SMALLINT  NULL ,
	sbmsn_cde            SMALLINT  NULL ,
	purp_cde             SMALLINT  NULL ,
	oblgns_amt_cum       NUMERIC(12,2)  NULL ,
	oblgns_cnt_cum       INTEGER  NULL ,
	vou_amt              NUMERIC(12,2)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.rda_fd_side
( 
	altmt                NUMERIC(12,2)  NULL ,
	altmt_1st_acctg_prd  NUMERIC(12,2)  NULL ,
	altmt_2nd_acctg_prd  NUMERIC(12,2)  NULL ,
	altmt_3rd_acctg_prd  NUMERIC(12,2)  NULL ,
	altmt_4th_acctg_prd  NUMERIC(12,2)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.rda_insrnc_authy
( 
	ppb_cde_1st          SMALLINT  NULL ,
	ppb_cde_2_3          SMALLINT  NULL ,
	sbmsn_cde            SMALLINT  NULL ,
	purp_cde             SMALLINT  NULL ,
	altmt                NUMERIC(12,2)  NULL ,
	oblgns_amt_cum       NUMERIC(12,2)  NULL ,
	oblgns_cnt_cum       INTEGER  NULL ,
	vou_amt              NUMERIC(12,2)  NULL ,
	altmt_1st_acctg_prd  NUMERIC(12,2)  NULL ,
	altmt_2nd_acctg_prd  NUMERIC(12,2)  NULL ,
	altmt_3rd_acctg_prd  NUMERIC(12,2)  NULL ,
	altmt_4th_acctg_prd  NUMERIC(12,2)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.rda_mallot
( 
	fy                   SMALLINT  NULL ,
	aproptn_cde          SMALLINT  NULL ,
	maj_cls              SMALLINT  NULL ,
	obj_clsfctn_cde      SMALLINT  NULL ,
	acct_typ_cde         SMALLINT  NULL ,
	multi_elmt_cde       SMALLINT  NULL ,
	ok_to_proc_cde       SMALLINT  NULL ,
	aprtnmts_cur_dtl     NUMERIC(12,2)  NULL ,
	altmt_cur            NUMERIC(12,2)  NULL ,
	aprtnmt_typ          SMALLINT  NULL ,
	altmt_typ            SMALLINT  NULL ,
	prd_cde              SMALLINT  NULL ,
	aprtnmts_1st_acctg_prd NUMERIC(12,2)  NULL ,
	aprtnmts_2nd_acctg_prd NUMERIC(12,2)  NULL ,
	aprtnmts_3rd_acctg_prd NUMERIC(12,2)  NULL ,
	aprtnmts_4th_acctg_prd NUMERIC(12,2)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.rda_mallot_oblgn
( 
	ppb_cde_1st          SMALLINT  NULL ,
	ppb_cde_2_3          SMALLINT  NULL ,
	sbmsn_cde            SMALLINT  NULL ,
	purp_cde             SMALLINT  NULL ,
	oblgns_amt_cum       NUMERIC(12,2)  NULL ,
	oblgns_cnt_cum       INTEGER  NULL ,
	vou_amt              NUMERIC(12,2)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.rda_rgn_dtl
( 
	fy                   SMALLINT  NULL ,
	rda_rgn_cde          SMALLINT  NULL ,
	aproptn_cde          SMALLINT  NULL ,
	maj_cls              SMALLINT  NULL ,
	obj_clsfctn_cde      SMALLINT  NULL ,
	acct_typ_cde         SMALLINT  NULL ,
	multi_elmt_cde       SMALLINT  NULL ,
	ok_to_proc_cde       SMALLINT  NULL ,
	distrbn_cur          NUMERIC(12,2)  NULL ,
	distrbn_typ_cde      SMALLINT  NULL ,
	prd_cde              SMALLINT  NULL  
);

CREATE TABLE IF NOT EXISTS farms.rda_rgn_oblgn
( 
	ppb_cde_1st          SMALLINT  NULL ,
	ppb_cde_2_3          SMALLINT  NULL ,
	sbmsn_cde            SMALLINT  NULL ,
	purp_cde             SMALLINT  NULL ,
	distrbn_cur          NUMERIC(12,2)  NULL ,
	oblgns_amt_cum       NUMERIC(12,2)  NULL ,
	oblgns_cnt_cum       INTEGER  NULL ,
	vou_amt              NUMERIC(12,2)  NULL ,
	distrbn_st_1st_acctg_prd NUMERIC(12,2)  NULL ,
	distrbn_st_2nd_acctg_prd NUMERIC(12,2)  NULL ,
	distrbn_st_3rd_acctg_prd NUMERIC(12,2)  NULL ,
	distrbn_st_4th_acctg_prd NUMERIC(12,2)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.reject_trnsctn
( 
	multi_card_data_lgth SMALLINT  NULL ,
	first_card_data      CHAR(150)  NULL ,
	multi_card_data      CHAR(1)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.rentl_cntrl
( 
	geog_st_cde_rentl_cntrl SMALLINT  NULL ,
	next_proj_nbr        INTEGER  NULL ,
	pymt_fctr_new        INTEGER  NULL ,
	pymt_fctr_exstg      INTEGER  NULL ,
	altmt_units_new      INTEGER  NULL ,
	oblgd_units_new      INTEGER  NULL ,
	altmt_units_exstg    INTEGER  NULL ,
	oblgd_units_exstg    INTEGER  NULL ,
	oblgn_long_term_cntrl NUMERIC(14,2)  NULL ,
	pymts_rentl          NUMERIC(13,2)  NULL ,
	oblgns_unlgdtd_cntrl NUMERIC(13,2)  NULL ,
	fam_unit_oblgd_ttl   NUMERIC(8)  NULL ,
	sr_cits_unit_oblgd_ttl NUMERIC(8)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.rentl_dtl
( 
	proj_nbr             INTEGER  NULL ,
	proj_typ_cde         SMALLINT  NULL ,
	ln_typ_cde           SMALLINT  NULL ,
	fy_pldgd_proj        SMALLINT  NULL ,
	fam_units_oblgd      SMALLINT  NULL ,
	sr_cits_units_oblgd  SMALLINT  NULL ,
	units_proj_ttl       SMALLINT  NULL ,
	units_lst_pymt       SMALLINT  NULL ,
	units_cur_fy_pd      SMALLINT  NULL ,
	lst_pymt_amt         NUMERIC(9,2)  NULL ,
	pymts_cur_fy         NUMERIC(9,2)  NULL ,
	pymts_cum            NUMERIC(9,2)  NULL ,
	oblgn_cur_fy         NUMERIC(10,2)  NULL ,
	oblgn_long_term      NUMERIC(10,2)  NULL ,
	oblgns_unlgdtd       NUMERIC(10,2)  NULL ,
	dte_oblgn_rentl      INTEGER  NULL ,
	dte_oblgn_rgstr      INTEGER  NULL ,
	dte_lst_ck           INTEGER  NULL ,
	dte_lst_ck_rgstr     INTEGER  NULL ,
	dte_int_asstnc       INTEGER  NULL ,
	rgstr_typ_lst_chng_rentl SMALLINT  NULL ,
	dte_lst_rgstr_dtl_rentl INTEGER  NULL ,
	fully_disbrsd_cde    CHAR(3)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.rentl_fy_unit
( 
	fy_units_oblgd       SMALLINT  NULL ,
	fam_units_oblgd_fy   SMALLINT  NULL ,
	sr_cits_units_fy     SMALLINT  NULL  
);

CREATE TABLE IF NOT EXISTS farms.rentl_ttl
( 
	typ_data_rentl_ttl   CHAR(3)  NULL ,
	oblgd_fam_amt        NUMERIC(12,2)  NULL ,
	oblgd_sr_cits_amt    NUMERIC(10,2)  NULL ,
	pymt_rcvd_amt        NUMERIC(12,2)  NULL ,
	oblgd_fam_units      INTEGER  NULL ,
	oblgd_sr_cits_units  SMALLINT  NULL ,
	units_pd_cur_yr      INTEGER  NULL ,
	projs_ttl            INTEGER  NULL  
);

CREATE TABLE IF NOT EXISTS farms.reschedule
( 
	dte_rvsd_pymt_agrmt_efctv INTEGER  NULL ,
	delq_amt_as_of_resched_agrmt NUMERIC(9,2)  NULL ,
	rvsd_pymt_instlmt_amt NUMERIC(7,2)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.rh_dfrl
( 
	rh_dfrd_mort_cde     SMALLINT  NULL ,
	pr_dfrd_amt          NUMERIC(7,2)  NULL ,
	cur_mo_dfrd_amt      NUMERIC(7,2)  NULL ,
	cur_anl_dfrd_amt     NUMERIC(7,2)  NULL ,
	dte_init_dfrl        INTEGER  NULL ,
	dte_cur_dfrl         INTEGER  NULL ,
	dte_cur_dfrl_exprtn  INTEGER  NULL ,
	dte_lst_cncltn       INTEGER  NULL ,
	cum_dfrd_prin_cr_amt NUMERIC(7,2)  NULL ,
	cum_dfrd_due_rcvb_amt NUMERIC(7,2)  NULL ,
	dfrd_prin_pd_amt     NUMERIC(7,2)  NULL ,
	cum_dfrd_int_cr_amt  NUMERIC(7,2)  NULL ,
	dfrd_int_pd_amt      NUMERIC(7,2)  NULL ,
	accrd_int_pd_amt     NUMERIC(7,2)  NULL ,
	cur_dfrd_mort_instlmt_amt NUMERIC(7,2)  NULL ,
	dte_lst_csh_cr       INTEGER  NULL ,
	non_csh_cr_amt       NUMERIC(7,2)  NULL ,
	sched_stat_dfrl      NUMERIC(7,2)  NULL ,
	cr_non_csh_appltn_typ_cde CHAR(1)  NULL ,
	dte_lst_non_csh_cr   INTEGER  NULL ,
	int_fcl_ln_dfrl      NUMERIC(7,2)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.site_lookup
( 
	cntct_nme_152        VARCHAR(25)  NULL ,
	mailg_adrs_line_1_152 VARCHAR(25)  NULL ,
	mailg_adrs_line_2_152 VARCHAR(25)  NULL ,
	mailg_adrs_line_3_152 VARCHAR(25)  NULL ,
	city_nme_152         VARCHAR(25)  NULL ,
	hq_twn_152           VARCHAR(20)  NULL ,
	st_abbr_1st_152      CHAR(1)  NULL ,
	st_abbr_2nd_152      CHAR(1)  NULL ,
	zip_cde_152          INTEGER  NULL ,
	zip_cde_lst_4_152    SMALLINT  NULL ,
	commrcl_152          VARCHAR(12)  NULL ,
	extension_152        VARCHAR(4) NULL ,
	fts_152              VARCHAR(12)  NULL ,
	fed_strip_152        VARCHAR(6)  NULL ,
	dte_updted_152       INTEGER  NULL ,
	updte_slctn_cde_152  CHAR(1)  NULL ,
	rmt_id_152           VARCHAR(8)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.srcfds
( 
	src_fds_cde          SMALLINT  NULL  
);

CREATE TABLE IF NOT EXISTS farms.st_lookup
( 
	st_cde_fmha          SMALLINT  NULL ,
	srvcg_ofc_cde_st     SMALLINT  NULL ,
	nme_st               VARCHAR(14)  NULL ,
	st_abbr              CHAR(2)  NULL ,
	hq_twn               VARCHAR(20)  NULL ,
	rgn_cde              SMALLINT  NULL ,
	st_ofc_cntrl_cde     SMALLINT  NULL  
);

CREATE TABLE IF NOT EXISTS farms.stat
( 
	stat_court_actn_pndg SMALLINT  NULL ,
	stat_frcl_actn_pndg  SMALLINT  NULL ,
	stat_bankruptcy      SMALLINT  NULL ,
	stat_3rd_party_jdgmt SMALLINT  NULL ,
	stat_trf_pndg        SMALLINT  NULL ,
	stat_subj_to_adjmt   SMALLINT  NULL ,
	stat_mrtm            SMALLINT  NULL ,
	dte_frcl_or_cnvync_actn SMALLINT  NULL ,
	stat_accltn          CHAR(1)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.stopper
(  
	id int not null
);

CREATE TABLE IF NOT EXISTS farms.subsidy
( 
	cur_sbsy_amt         INTEGER  NULL ,
	pr_sbsy_amt          INTEGER  NULL ,
	prin_cr_sbsy         NUMERIC(9,2)  NULL ,
	int_cr_sbsy          NUMERIC(9,2)  NULL ,
	int_asstnc_cum_amt   NUMERIC(9,2)  NULL ,
	sbsy_recptr_cde      SMALLINT  NULL ,
	efctv_mo_sbsy_agrmt  SMALLINT  NULL ,
	efctv_day_sbsy_agrmt SMALLINT  NULL ,
	efctv_yr_sbsy_agrmt  SMALLINT  NULL ,
	exprtn_mo_sbsy_agrmt SMALLINT  NULL ,
	exprtn_day_sbsy_agrmt SMALLINT  NULL ,
	exprtn_yr_sbsy_agrmt SMALLINT  NULL ,
	mo_sbsy_cnvsn        SMALLINT  NULL ,
	day_sbsy_cnvsn       SMALLINT  NULL ,
	yr_sbsy_cnvsn        SMALLINT  NULL ,
	prin_redctn_sbsy     NUMERIC(9,2)  NULL ,
	unpd_prin_cnvsn      NUMERIC(9,2)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.subsrc
( 
	cohort_cde           SMALLINT  NULL ,
	src_fds_cde          SMALLINT  NULL  
);

CREATE TABLE IF NOT EXISTS farms.trnsctn_cntrl
( 
	trnsctn_cntrl_key    CHAR(2)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.trnsctn_rvrsl
( 
	trnsctn_cde_updte    CHAR(2)  NULL ,
	ln_amt               NUMERIC(9,2)  NULL ,
	recvrbl_cst_chgs     NUMERIC(9,2)  NULL ,
	prin_cr_ln           NUMERIC(9,2)  NULL ,
	int_cr_ln            NUMERIC(9,2)  NULL ,
	int_fcl_ln           NUMERIC(9,2)  NULL ,
	chgs_advnc_from_fd   NUMERIC(9,2)  NULL ,
	prin_cr_advnc_from_fd NUMERIC(9,2)  NULL ,
	int_cr_advnc_from_fd NUMERIC(9,2)  NULL ,
	int_fcl_from_advnc_dte NUMERIC(9,2)  NULL ,
	insrnc_chgs_cum_amt  NUMERIC(7,2)  NULL ,
	prin_cr_insrnc_chg_cum NUMERIC(7,2)  NULL ,
	st_cde_trfee         SMALLINT  NULL ,
	cty_cde_trfee        SMALLINT  NULL ,
	id_nbr_trfee         NUMERIC(10)  NULL ,
	fd_cde_2             SMALLINT  NULL ,
	fd_cde_3rd           SMALLINT  NULL ,
	fd_cde_4th           SMALLINT  NULL ,
	ln_nbr               SMALLINT  NULL ,
	procg_typ_cde        CHAR(1)  NULL ,
	dfrd_int_ln_amt      NUMERIC(8,2)  NULL ,
	non_cptlzd_int_ln_amt NUMERIC(9,2)  NULL ,
	dfrd_non_cptlzd_int_amt NUMERIC(9,2)  NULL ,
	cptlzd_int           NUMERIC(9,2)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.trrate
( 
	trsry_yr             SMALLINT  NULL ,
	mturty_rnge_cde      SMALLINT  NULL ,
	qtr_rate             NUMERIC(4,4)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.trstr
( 
	trsry_yr             SMALLINT  NULL ,
	mturty_rnge_cde      SMALLINT  NULL ,
	trsry_sym_cde        VARCHAR(7)  NULL ,
	cohort_cde           SMALLINT  NULL  
);

CREATE TABLE IF NOT EXISTS farms.user_authy
( 
	trnsctn_authy_cde    CHAR(2)  NULL ,
	trnsctn_cnt          CHAR(3)  NULL ,
	trnsctn_cde_updte    CHAR(2)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.user_domain
( 
	dte_lst_updte        INTEGER  NULL ,
	st_cde_fmha          SMALLINT  NULL ,
	cty_cde_fmha         SMALLINT  NULL ,
	nme_cty              VARCHAR(20)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.user_statcs
( 
	rpt_rqst_cde         CHAR(1)  NULL ,
	lst_lgn_dte          INTEGER  NULL ,
	trnsctn_ttl_cnt      NUMERIC(7)  NULL ,
	hr_start             SMALLINT  NULL ,
	min_start            SMALLINT  NULL ,
	optn_cde             CHAR(1)  NULL ,
	accmltd_time_dtd     NUMERIC(6,2)  NULL ,
	trnsctn_ttl_cnt_dtd  NUMERIC(7)  NULL ,
	accmltd_time_mtd     NUMERIC(6,2)  NULL ,
	trnsctn_ttl_cnt_mtd  NUMERIC(7)  NULL ,
	accmltd_time_ytd     NUMERIC(6,2)  NULL ,
	trnsctn_ttl_cnt_ytd  NUMERIC(7)  NULL  
);

CREATE TABLE IF NOT EXISTS farms.users
( 
	user_id_alt          VARCHAR(6)  NULL ,
	srvcg_ofc_cde_cty    INTEGER  NULL ,
	orgztn_struc         SMALLINT  NULL ,
	scrty_indctr_cde     SMALLINT  NULL ,
	trnsctn_authy_cde    CHAR(2)  NULL  
);
