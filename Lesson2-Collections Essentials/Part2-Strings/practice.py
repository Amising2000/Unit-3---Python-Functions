# 3
def create_username(first_name, last_name):
    return f"{first_name}_{last_name}".lower()

print(create_username('John', 'Smith'))

# 4
def check_email(email):
    if '@' in email.lower() and '.com' in email.lower():
        return True
    else:
        return False

print(check_email('test@gmail.com'))
print(check_email('user@gmail.COM'))
print(check_email('invalid.com'))
print(check_email('test@school.edu'))


def create_slug(title):
    return title.strip().lower().replace(' ', '-')

print(create_slug('My first Blog post'))