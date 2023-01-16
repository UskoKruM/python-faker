from faker import Faker
from faker.providers import bank, company, internet, person

fake = Faker()
fake.add_provider(bank)
fake.add_provider(company)
fake.add_provider(internet)
fake.add_provider(person)

for _ in range(10):
    # print(fake.name())
    # print(fake.address())
    # print(fake.text())
    # print(fake.first_name())
    # print(fake.bban())
    # print(fake.company())
    # print(fake.ipv6())
    print(fake.email())
