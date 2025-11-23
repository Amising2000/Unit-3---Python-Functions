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
        pasre = int(string)
        return
    except:
        return None