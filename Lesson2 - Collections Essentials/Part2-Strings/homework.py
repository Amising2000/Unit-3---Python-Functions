# 1
'john.smith, gmail.com'

# 2
'tqbf'

# 3
def extract_domain(email):
    count = email.count('@')
    if not count == 1:
        return 'invalid email'
    domain = (email.split('@')[1]).lower()
    return domain
print(extract_domain('john@gmail.com'))
print(extract_domain('jJANE@YAHOO.COM'))
print(extract_domain('missing.at.sign.com'))
print(extract_domain('too@@many@signs.com'))

# 4
'123456'

# 5
'MY_DOCUMENT'

# 6
'banana'

# 7
def filter_numbers(text):
    filter = ''
    for letter in text:
        if not letter.isdigit():
            filter += letter
    return f'"{filter}"'
print(filter_numbers('Hello123World456'))
print(filter_numbers('Test 1 2 3'))
print(filter_numbers('Price: $29.99'))
print(filter_numbers('No numbers here!'))

# 8
'https://example.com/users/profile'

# 9
def count_character_types(text):
    letters = 0
    digits = 0
    spaces = 0
    for char in text:
        if char == ' ':
            spaces += 1
        elif char.isdigit():
            digits += 1
        else:
            letters += 1
    return {
        "letters": letters,
        "digits": digits,
        "spaces": spaces
    }
print(count_character_types("Hello 123"))
print(count_character_types("Test2024!~"))