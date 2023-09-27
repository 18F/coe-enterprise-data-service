from mimesis import Person, Address, Datetime, Generic
from mimesis.locales import Locale
# , Business
import pandas as pd
import random
import string

def generate_client_data(num_data):
    # person = Person('en')
    person = Person(locale=Locale.EN)
    address = Address('en')
    datetime = Datetime('en')
    generic = Generic('en')
    # business = Business('en-us')

    string.ascii_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    mailing_level_code = ['S','D','C','T','U','V']
    fips_list = open("./state_county_fip.txt").read().splitlines() # .readlines()

    client_data = []
    for _ in range(num_data):
        client = {
            "CASE-NBR": generic.random.choice(fips_list) + str(generic.random.randint(1000000, 8999990)).rjust(10, "0"),
            "CASE-NBR-OBLR":generic.random.choice(fips_list),
            "MAILG-LVL-CLIENT": generic.random.choice(mailing_level_code),
            "MAILG-CDE-CLIENT": generic.random.choice(fips_list),
            "NME-FLDS-BORR-CNT": generic.random.randint(1,3),
            "ADRS-FLDS-BORR-CNT":generic.random.randint(1,3),
            "NME-OBLR":person.full_name(),
            "NME-ADRS-OBLR-1":address.address(),
            "NME-ADRS-OBLR-2":person.full_name(),
            "NME-OBLR-KEY": generic.random._randstr(length=20),
            "NME-ADRS-OBLR-3": address.city(),
            "NME-ADRS-OBLR-4":address.province(), # generic.random._randstr(length=19), 
            "ZIP-CDE":address.postal_code(),
            "RACE-DESC-CDE":generic.random.randint(1,8),
            "SEX-CDE":generic.random.randint(1,8),
            "MRTL-STAT":generic.random.randint(1,4),
            "TAX-EXEMPT-CDE":generic.random.randint(1,5),
            "VET-CDE": generic.random.randint(1,4),
            "DUE-DAY-PYMT":str(generic.random.randint(1, 28)).rjust(2, "0"),
            "APPLT-TYP-CDE": generic.random.randint(1,8),
            "NET-WORTH-AMT": (round(generic.random.uniform(100000, 5000000),2)),
            "LN-NBR-LST-ASGD":generic.random.randint(10, 90),
            "RCRD-LN-CNT": str(generic.random.randint(0, 5)).rjust(2, "0"),
            "LN-CNT-EE":generic.random.randint(0, 1),
            "LN-CNT-OTC":generic.random.randint(0, 1),
            "LN-CNT-INSRD-FO":generic.random.randint(0, 1),
            "LN-CNT-DIR-FO":generic.random.randint(0, 1),
            "LN-CNT-INSRD-SW":generic.random.randint(0, 1),
            "LN-CNT-DIR-SW":generic.random.randint(0, 1),
            "LN-CNT-INSRD-RH":generic.random.randint(0, 1),
            "LN-CNT-DIR-RH":generic.random.randint(0, 2),
            "LN-CNT-INVSTR":generic.random.randint(0, 2),
            "LN-CNT-ASSOC":generic.random.randint(0, 2),
            "SUSP-CDE-ACCT":generic.random.randint(0, 2),
            "DTE-LST-RGSTR-ACCT":datetime.date(start=2011, end=2021).isoformat(),
            "RGSTR-TYP-LST-TRNSCTN":str(generic.random.randint(1, 88)).rjust(2, "0"),
            "SIS-TRF-CDE":random.choice(string.ascii_letters),
            "EMPL-RELTNSHP-CDE":random.choice(string.ascii_letters),
            "LRTF-SRVCG-CDE":generic.random.randint(2, 8),
            "MAILG-OFC-FSA": generic.random.choice(mailing_level_code),
            "MAILG-CDE-FSA": generic.random.choice(fips_list),
            "ORGZTN-CDE":random.choice(string.ascii_letters),
            "DTE-OAC-ESTBD":datetime.date(start=2000, end=2014).isoformat(),
            "DTE-OAC-RSLVD":datetime.date(start=2005, end=2019).isoformat(),
            "DTE-OAC-MRTM-EFCTV": datetime.date(start=2015, end=2020).isoformat(),
            "PREVL-INDCTR":generic.random.randint(0, 4),
            "NBR-COMPLNTS": random.choice(string.ascii_letters),


            # "dstr_dclrd_cde":generic.random.randint(1, 9),
            # "mrg_cntrl":generic.random.randint(10, 90),
            # # "docmt_typ_cde": generic.random._randstr(False,1),
            # "docmt_typ_cde":random.choice(mailing_level_code),
            # "dte_oblgn_ln":datetime.date(start=2011, end=2021).isoformat(),
            # "asstnc_typ_cde":generic.random.randint(100, 950),
            # "ln_amt_oblgn":(round(generic.random.uniform(10000, 500000),2)),
            # # "begng_frmr_rnchr_cde":generic.random._randstr(False, 1),
            # "begng_frmr_rnchr_cde":random.choice(mailing_level_code),
            # "colltl_cde":generic.random.randint(1, 9),
            # "cpn_procg_dte":datetime.date(start=2012, end=2022).isoformat(),
            # "case_nbr_chng_cde":generic.random.randint(0, 9),
            # "pymt_asstnc_meth_cde":generic.random.randint(0, 9),
            # "int_rate_prev":(round(generic.random.uniform(5, 15),4)),
            # "int_rate_prev_redfnd":(round(generic.random.uniform(5, 19),4)),



            # "name": person.full_name(),
            # "email": person.email(),
            # "phone": person.telephone(),
            # "address": address.address(),
            # "city": address.city(),
            # "country": address.country(),
            # "birth_date": datetime.date(start=1960, end=2000).isoformat(),
            # "gender": person.gender(),
            # "ssn": person.identifier('ssn'),
            
            # "loan_amount": (generic.random.uniform(10000, 5000000)),
            # "interest_rate": (round(generic.random.uniform(1, 15),2)),
            # "loan_effective_date": datetime.date(start=2010, end=2020).isoformat(),
            # "registered_at": datetime.datetime(start=2010, end=2020).isoformat(),
            # # "lender": business.company(),
        }
        client_data.append(client)

    return client_data

# Generate 5000 fake clients
num_data = 5000
fake_acct_data = generate_client_data(num_data)

# Convert customer data to DataFrame
df = pd.DataFrame(fake_acct_data)

# Convert DataFrame to comma-delimited (CSV) file
csv_file = './client_data.csv'
df.to_csv(csv_file, index=False)

print(f"CSV file '{csv_file}' has been created.")