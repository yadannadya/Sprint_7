from faker import Faker

faker = Faker()

def faker_courier():
    return {
        "login": faker.name(),
        "password": faker.password(length = 10, special_chars=True, digits=True, upper_case=True, lower_case=True),
        "firstName": faker.first_name()
        }

