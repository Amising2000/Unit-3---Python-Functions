def calculate_discount(p, m):
    if m == "premium":
        return p * .7
    elif m == "standard":
        return p * .85
    else:
        return p
    
print(calculate_discount(10, "premium"))

def count_vowels(text):
    
    count = 0
    # for char in text:
    #     if char == "A" or char == "a" or char == "E" or char == "e" or char == "I" or char == "i" or char == "O" or char == "o" or char == "U" or char == "u":
    #         count += 1
    
    vowels = "aeiouAEIOU"
    for char in text:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Hello, World"))
print(count_vowels("Python"))
print(count_vowels("AEioU"))

def validate_password(password):
    if len(password) < 8:
        return False
    
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            
    return has_digit 