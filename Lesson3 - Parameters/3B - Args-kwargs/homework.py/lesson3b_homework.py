# 1
def combine_values(*values):
    combined = 1
    if not values:
        return combined
    else:
        for value in values:
            combined *= value
        return combined


print(combine_values(2, 3, 4))  # → 24
print(combine_values(5))  # → 5
print(combine_values())  # → 1


# 2
def merge_details(label, **extra):
    result = {"label": label}
    result.update(extra)
    return result


print(merge_details("ItemA", size="Large", cost=12.50))
# → {"label": "ItemA", "size": "Large", "cost": 12.50}
print(merge_details("UserX"))
# → {"label": "UserX"}


# 3
8
10
0


# 4
{"name": "Alpha", "x": 1, "y": 2, "count": 2}
{"name": "Beta", "count": 0}