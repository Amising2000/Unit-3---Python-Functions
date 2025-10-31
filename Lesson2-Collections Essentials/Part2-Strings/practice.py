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


# 3
def format_phone_number(phone):
    cleaned_number = ''
    for num in phone:
        if num.isdigit():
            cleaned_number += num
    if not len(cleaned_number) == 10:
        return 'Invalid phone number'
    return f"({cleaned_number[0:3]}) {cleaned_number[3:6]}-{cleaned_number[6:]}"
print(format_phone_number('555-123-6578'))