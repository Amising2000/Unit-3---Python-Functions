# 15
def calculate_average(numbers):
    total = sum(numbers)
    try:
        average = total / len(numbers)
    except:
        average = 0
    return average

grades = []
result = calculate_average(grades)
print(f"Average: {result}")


# 16
"C"


# 17
text = " Hello Python World "

# Remove whitespace from both ends
clean = text.strip()

# Convert to uppercase
upper = text.upper()

# Split into a list of words
words = text.strip().split()

# Get the length of the cleaned text
length = len(text.strip())


# 18
def validate_password(password):
    # if password:
    #     is_valid = True
    #     message = 'Valid'
    #     if len(password) < 8:
    #         is_valid = False
    #         message = "Too short"
    # else:
    #     is_valid = False
    #     message = "Empty password"
    # return is_valid, message

    if not password:
        return False, "Empty password"
    if len(password) < 8:
        return False, "Too short"
    return True, "Valid"


# 19
def create_inventory(item_name, *quantities, location="Warehouse"):
    total = sum(quantities) if quantities else 0
    return {
    "item": item_name,
    "total": total,
    "location": location
    }


# 20
def safe_list_access(items, index):
    try:
        value = items[index]
        return value, True
    except IndexError:
        return None, False