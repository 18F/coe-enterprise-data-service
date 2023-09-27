from mimesis import Person, Address, Datetime, Generic
from mimesis.locales import Locale
# , Business
import pandas as pd
import random
import string

def generate_loan_data(num_data):
    # person = Person('en')
    person = Person(locale=Locale.EN)
    address = Address('en')
    datetime = Datetime('en')
    generic = Generic('en')
    # business = Business('en-us')

    string.ascii_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    purchase_code = ['S','D','C','T','U','V']
    installment_type = ['W','M','Q','A','S']
    fips_list = open("./state_county_fip.txt").read().splitlines() # .readlines()

    loan_data = []
    for _ in range(num_data):
        loan = {
            "INT-RATE-BORR": (round(generic.random.uniform(1, 15),4)),  # generic.random.choice(fips_list) + str(generic.random.randint(1000000, 8999990)).rjust(10, "0"),
            "INT-RATE-BORR-1ST":(round(generic.random.uniform(1, 15),4)), #generic.random.choice(fips_list),
            "APPLTN-CDE": generic.random.randint(1,3),
            "FULLY-PD-CDE":generic.random.randint(0,1),
            "FULLY-MTURD-CDE":generic.random.randint(0,2),
            "ADVNC-UNCLSD-CDE":generic.random.randint(0,3),
            "ACT-COLLCTN-ONLY-CDE":generic.random.randint(0,1),
            "ASSOC-TYP-NOTE-CDE":generic.random.randint(0,1),
            "PURCH-CDE":generic.random.choice(purchase_code),
            "NBR-PYMTS-AMORTN":str(generic.random.randint(10, 300)).rjust(3, "0"),
            "INSTLMTS-INT-ONLY-CNT":generic.random.randint(1,6),
            "SALE-STAT-CDE":generic.random.randint(1,4),
            "FIXD-PRD-INIT-LGTH":generic.random.randint(10,50),
            "MORT-HLDR-CDE":generic.random.randint(60,80),
            "YR-LN-CLSD":generic.random.randint(20,20),
            "DTE-LN-SLD-OR-PLDGD":datetime.date(start=2011, end=2021).isoformat(),
            "FMHA-DIR-TO-INSRD-CDE":generic.random.randint(0,1),
            "DTE-CLSG":datetime.date(start=2011, end=2021).isoformat(),
            "DTE-LN-EXPRTN":datetime.date(start=2041, end=2051).isoformat(),
            "LN-AMT":(round(generic.random.uniform(100000, 5000000),2)),
            "RECVRBL-CST-CHGS":(round(generic.random.uniform(10000, 50000),2)),
            "PRIN-CR-LN":(round(generic.random.uniform(10000, 50000),2)),
            "INT-CR-LN":(round(generic.random.uniform(10000, 50000),2)),
            "INT-FCL-LN":(round(generic.random.uniform(10000, 50000),2)),
            "SCHED-STAT":(round(generic.random.uniform(10000, 50000),2)),
            "PYMT-EXTRA-AMT-CUM":(round(generic.random.uniform(20000, 70000),2)),
            "CR-NON-CSH-APPLTN-TYP-CDE":random.choice(string.ascii_letters),
            "CR-NON-CSH-LST-AMT-APPLD":(round(generic.random.uniform(30000, 90000),2)),
            "DTE-LST-NON-CSH-CR":datetime.date(start=2013, end=2019).isoformat(),
            "DTE-LST-CSH-CR":datetime.date(start=2013, end=2019).isoformat(),
            "DTE-NEXT-INSTLMT-DUE":datetime.date(start=2013, end=2019).isoformat(),
            "INSTLMT-DUE-NEXT-AMT":(round(generic.random.uniform(1000, 4000),2)),
            "INSTLMT-NEXT-TYP-CDE":generic.random.randint(1,6),
            "MTURD-CDE-DIR-RE":generic.random.randint(1,3),
            "DTE-INSTLMT-DUE":datetime.date(start=2012, end=2022).isoformat(),
            "INSTLMT-DUE-AMT":(round(generic.random.uniform(1000, 4000),2)),
            "INSTLMT-TYP-CDE":generic.random.choice(installment_type),
            "MTURD-CDE-DIR-RE":generic.random.randint(4,7),
            "SUSP-CDE-LN": generic.random.randint(5,9),
            "DTE-LST-RGSTR-DTL":datetime.date(start=2010, end=2020).isoformat(),
            "RGSTR-TYP-LST-CHNG": generic.random.randint(20,40),
            "LN-NBR-OLD": str(generic.random.randint(1,99)).rjust(2, "0"),
            "INT-ASSTNC-CDE":generic.random.randint(1,5),
            "WRTF-CDE":random.choice(string.ascii_letters),
        }
        loan_data.append(loan)

    return loan_data

# Generate 5000 fake clients
num_data = 5000
fake_loan_data = generate_loan_data(num_data)

# Convert customer data to DataFrame
df = pd.DataFrame(fake_loan_data)

# Convert DataFrame to comma-delimited (CSV) file
csv_file = './loan_data.csv'
df.to_csv(csv_file, index=False)

print(f"CSV file '{csv_file}' has been created.")