def search_data(query):
    if query == "":
        return None
    if query == "empty":
        return 0
    if query == "error":
        return False
    return len(query)

# Return Type - None -> "No Value"
# Meaning: Absense of value, not set, not found
# Uses for : Missing Data, search failures, optional parameters
result = None
print(result is None) #True - identity check
print(result == None) #True - equality check
print(not result) #True - falsy check

# 2 Return Type - False = Boolean False
# Meaning: Explicit false condition, validation failure, negative result
# Use for: Validation result, boolean operations, success/failure status
result = False
print(result is False) #True - identity check
print(not result) #True - boolean negation
print(result == 0) #True - falsy check

# 3 Return Zero - A valid Number
# Zero is VALID numeric value, not absense of value!
result = 0
print(result == 0) #True - numeric equality
print(not result) #True - (falsy in boolean context)
print(result is None) #False - different objects
print(result is False) #False - different types

# 4 Multiple Returns - python packs multiple returns into a tuple
def calculate(l, w):
    area = l * w
    perimeter = 2 * (l + w)
    return area, perimeter

result = calculate(6, 7)
print(result)
print(type(result))


print(type((42))) # int
print(type((42, ))) # tuple for single item
no_parentheses = 1, 2, 3
print(type(no_parentheses))


# unpacking tuple
area_result, perimeter_result = calculate(20, 6)
print(f"Area: {area_result}")
print(f"Perimeter: {perimeter_result}")



def calc_stats(*grades):
    if not grades:
        return 0, 0, 0, False
    average = sum(grades) / len(grades)
    lowest = min(grades)
    highest = max(grades)
    if average >= 60:
        return average, highest, lowest, True
    else:
        return average, highest, lowest, False

print(calc_stats(85, 92, 78, 90))