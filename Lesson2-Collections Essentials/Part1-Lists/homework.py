def remove_duplicates(items):
    duplicates = []
    for item in items:
        if item not in duplicates:
            duplicates.append(item)
    return duplicates


print(remove_duplicates([1, 2, 2, 3, 1, 4]))
print(remove_duplicates(["a", "b", "a", "c"]))
print(remove_duplicates([5, 5, 5]))
print(remove_duplicates([]))

print("-" * 40)


def find_common(list1, list2):
    common = []
    for item1 in list1:
        for item2 in list2:
            if item1 == item2 and item1 not in common:
                common.append(item1)
    return common


print(find_common([1, 2, 3], [2, 3, 4]))
print(find_common(["a", "b"], ["c", "d"]))
print(find_common([1, 1, 2], [2, 2, 3]))
print(find_common([], [1, 2]))

print("-" * 40)
