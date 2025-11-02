# day1
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


print('-' * 50)


# day2
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


print('-' * 50)


# day3
# QUESTION 6: Code Writing - sanitize_filename
def sanitize_filename(filename):
# My way
    clean = filename.strip().lower().replace(" ", "_")
    sanitized = ""
    for char in clean:
        if char.isalnum() or char in  '.-_':
            sanitized += char
    if not sanitized.endswith(".txt"):
        if len(sanitized) > 46:
            sanitized = sanitized[:46]
            sanitized += '.txt'
            return f"Length Modified: {sanitized}"
        sanitized += '.txt'
    return sanitized

# Method 1
    # '''Clean and format a filename for safe use.'''
    # #Step 1: To lowercase
    # clean = filename.lower()
    # #Step 2: Spaces to underscores
    # clean = clean.replace("", "_")
    # # Step 3: Keep only allowed characters
    # allowed = ''
    # for char in clean:
    #     if char.isalnum() or char in ".-_":
    #         allowed += char
    # #Step 4: Handle .txt extension
    # if allowed.endswith(".txt"):
    #     result = allowed
    # else:
    #     if "." in allowed:
    #         dot_pos = allowed.rfind(".")
    #         allowed = allowed[:dot_pos]
    # result = allowed + ".txt"
    # #Step 5: Max 50 characters
    # if len(result) > 50:
    #     max_base = 504 #50 4 for ".txt"
    #     result = result[:max_base] + ".txt"
    # return result

# Method 2
    # """Clean and format a filename for safe use."""
    # # Lowercase and replace spaces
    # clean = filename.lower().replace(" ", "_")
    # # Keep safe characters
    # safe = ''
    # for char in clean:
    #     if char.isalnum() or char in ".-_":
    #         safe += char
    # # Handle extension
    # if not safe.endswith(".txt"):
    #     if "." in safe:
    #         safe = safe[:safe.rfind(".")]
    #     safe += ".txt"
    # # Truncate
    # if len(safe) > 50:
    #     safe = safe[:46] + ".txt" #46 + 4 = 50
    # return safe
    

print(sanitize_filename('Ancient Scroll.txt'))
print(sanitize_filename('Quest 2024! (Epic)'))
print(sanitize_filename('notes'))
print(sanitize_filename('X' * 60))