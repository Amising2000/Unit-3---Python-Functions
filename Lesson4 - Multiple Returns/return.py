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