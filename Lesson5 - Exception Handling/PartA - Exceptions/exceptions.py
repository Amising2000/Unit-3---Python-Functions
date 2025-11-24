def safe_divide(x, y):
    try:
        result = x / y
        return result
    # except:
    #     print("Cannot Divide by Zero!")
    #     return None
    except ZeroDivisionError:
        print("Cannot Divide by Zero!")
        return None
    except TypeError:
        print("That's Not A Valid Number!")
        return None
    except:
        print("An error has occured...")
        return None

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide(10, "hello"))


def safe_operations(a, b, lst, key, d):
    try:
        print(f"Divition results: {a/b}")
        TypeError
        print("Access List Element:", lst[2])
        print("Access Dictionary Key:", d[key])
        print("Add Numbers: {a + b}")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except IndexError:
        print("List index out of range!")
    except KeyError:
        print(f"Key {key} not found in dictionary!")
    except TypeError:
        print("Invalid types for operation!")
    except Exception as e:
        print("Some other error occured", e)

print(safe_operations(10, 2, [1, 2], "Tom", {"John": 15}))


# 1
def calculate_price_per_item(total_cost, num_items):
    try:
        result = total_cost / num_items
    except Exception as e:
        result =  print("Some error occured:", e)
    return result

print(calculate_price_per_item(100, 4))
print(calculate_price_per_item(50, 0))
print(calculate_price_per_item(25.50, 3))


# 2
def parse_age(string):
    try:
        parse = int(string)
        return parse
    except:
        return None


# 3
def get_phone_number(contacts, name):
    try:
        return contacts[name]
    except KeyError:
        return "Contact not found"


contacts = {"Mom": "555-0123", "Dad": "555-0124", "Best Friend": "555-0125"}
print(get_phone_number(contacts, "Mom"))
# Output: "555-0123"

contacts = {"Mom": "555-0123", "Dad": "555-0124", "Best Friend": "555-0125"}
print(get_phone_number(contacts, "Boss"))
# Output: "Contact not found"

contacts = {"Mom": "555-0123", "Dad": "555-0124", "Best Friend": "555-0125"}
print(get_phone_number(contacts, "Best Friend"))
# Output: "555-0125"


# 4
def get_song(playlist, position):
    try:
        return playlist[position]
    except IndexError:
        return "Position out of range"
    except TypeError:
        return "Position must be an integer"

playlist = ["Song A", "Song B", "Song C", "Song D", "Song E"]
print(get_song(playlist, 2))
# Output: "Song C"

playlist = ["Song A", "Song B", "Song C", "Song D", "Song E"]
print(get_song(playlist, 20))
# Output: "Position out of range"

playlist = ["Song A", "Song B", "Song C", "Song D", "Song E"]
print(get_song(playlist, "first"))
# Output: "Position must be an integer"


# 5
def calculate_test_average(scores):
    try:
        return round(sum(scores) / len(scores), 2)
    except ZeroDivisionError:
        return 0
    except TypeError:
        return "Invalid score data"

print(calculate_test_average([88, 92, 76, 95, 84]))
# Output: 87.0

print(calculate_test_average([78.5, 92.0, 85.5]))
# Output: 85.33

print(calculate_test_average([]))
# Output: 0