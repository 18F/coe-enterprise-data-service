from mimesis import Person, Address, Datetime, Generic
from mimesis.locales import Locale
# , Business
import pandas as pd

def generate_customer_data(num_customers):
    # person = Person('en')
    person = Person(locale=Locale.EN)
    address = Address('en')
    datetime = Datetime('en')
    generic = Generic('en')
    # business = Business('en-us')

    customers = []
    for _ in range(num_customers):
        customer = {
            "name": person.full_name(),
            "email": person.email(),
            "phone": person.telephone(),
            "address": address.address(),
            "city": address.city(),
            "country": address.country(),
            "birth_date": datetime.date(start=1960, end=2000).isoformat(),
            "gender": person.gender(),
            "ssn": person.identifier('ssn'),
            "loan_number": generic.random.randint(100000, 999999),
            "loan_amount": (generic.random.uniform(10000, 5000000)),
            "interest_rate": (round(generic.random.uniform(1, 15),2) ),
            "loan_effective_date": datetime.date(start=2010, end=2020).isoformat(),
            "registered_at": datetime.datetime(start=2010, end=2020).isoformat(),
            # "lender": business.company(),
        }
        customers.append(customer)

    return customers

# Generate 10 fake customers
num_customers = 1000
fake_customers = generate_customer_data(num_customers)

# Convert customer data to DataFrame
df = pd.DataFrame(fake_customers)

# Convert DataFrame to comma-delimited (CSV) file
csv_file = './customer_data.csv'
df.to_csv(csv_file, index=False)

print(f"CSV file '{csv_file}' has been created.")

# # Define the field widths for each attribute
# field_widths = {
#     "name": 30,
#     "email": 50,
#     "phone": 15,
#     "address": 50,
#     "city": 20,
#     "country": 30,
#     "birth_date": 10,
#     "gender": 10,
#     "ssn": 15,
#     "loan_number": 10,
#     "loan_amount": 10,
#     "interest_rate": 10,
#     "loan_effective_date": 10,
#     "registered_at": 20,
#     # "lender": 50,
# }

# # Convert customer data to DataFrame
# df = pd.DataFrame(fake_customers)

# # Convert DataFrame to fixed-width format with left padding
# fixed_width_data = ''
# for _, row in df.iterrows():
#     fixed_width_row = ''
#     for col, width in field_widths.items():
#         value = str(row[col])
#         if isinstance(row[col], int) or isinstance(row[col], float):
#             value = value.zfill(width)
#         else:
#             value = value.ljust(width)[:width]
#         fixed_width_row += value
#     fixed_width_data += fixed_width_row + '\n'

# # Write fixed-width data to file
# with open('./customer_data.txt', 'w') as f:
#     f.write(fixed_width_data)

# print(df)

# https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa0p3ejZkZWdheDluaFBPODNoNjRRYlVaT1BEZ3xBQ3Jtc0tsT3FZVVZjaG9BTzFocUNEWVA4UmE0aFFFdzVUNnpyTDhIUlVBZjB4TE1jTmI5REVLQmVRbjNmWUFtLUZWdC0ycjU5eW5hcERoZlowdkpNY3R3UWJ6MkdRNjdwRWZ3RFdWX1Y1bXI5a1I1clE2Mjkybw&q=https%3A%2F%2Fdeveloper.hashicorp.com%2Fterraform%2Ftutorials%2Faws%2Faws-rds&v=pSmip5pOAVM