from mimesis import Person, Address, Datetime, Generic
from mimesis.locales import Locale
# , Business
import pandas as pd
import random

def generate_account_data(num_data):
    # person = Person('en')
    person = Person(locale=Locale.EN)
    address = Address('en')
    datetime = Datetime('en')
    generic = Generic('en')
    # business = Business('en-us')
    document_type_list = ['A','B','C','D','E','F','G']
    farmer_rancher_code = ['F','O','R','W']

    account_data = []
    for _ in range(num_data):
        account = {
            "ln_nbr": generic.random.randint(100000, 899999),
            "fd_cde": generic.random.randint(0, 9),
            "kind_cde_ln": generic.random.randint(0, 9),
            "int_rate_note": (round(generic.random.uniform(1, 15),4)),
            "int_rate_note_1st":(round(generic.random.uniform(5, 18),4)),
            "pymt_typ_cde":generic.random.randint(1, 9),
            "dir_pymt_cde":generic.random.randint(0, 9),
            "dte_amortn_efctv":datetime.date(start=2010, end=2020).isoformat(),
            "dstr_dclrd_cde":generic.random.randint(1, 9),
            "mrg_cntrl":generic.random.randint(10, 90),
            # "docmt_typ_cde": generic.random._randstr(False,1),
            "docmt_typ_cde":random.choice(document_type_list),
            "dte_oblgn_ln":datetime.date(start=2011, end=2021).isoformat(),
            "asstnc_typ_cde":generic.random.randint(100, 950),
            "ln_amt_oblgn":(round(generic.random.uniform(10000, 500000),2)),
            # "begng_frmr_rnchr_cde":generic.random._randstr(False, 1),
            "begng_frmr_rnchr_cde":random.choice(farmer_rancher_code),
            "colltl_cde":generic.random.randint(1, 9),
            "cpn_procg_dte":datetime.date(start=2012, end=2022).isoformat(),
            "case_nbr_chng_cde":generic.random.randint(0, 9),
            "pymt_asstnc_meth_cde":generic.random.randint(0, 9),
            "int_rate_prev":(round(generic.random.uniform(5, 15),4)),
            "int_rate_prev_redfnd":(round(generic.random.uniform(5, 19),4)),



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
        account_data.append(account)

    return account_data

# Generate 10 fake customers
num_data = 5000
fake_acct_data = generate_account_data(num_data)

# Convert customer data to DataFrame
df = pd.DataFrame(fake_acct_data)

# Convert DataFrame to comma-delimited (CSV) file
csv_file = './account_data.csv'
df.to_csv(csv_file, index=False)

print(f"CSV file '{csv_file}' has been created.")