def filter_events(numbers):
    evens = []
    for n in numbers:
        if n % 2 == 0:
            evens.append(n)
    return evens

print(filter_events([1, 2, 3, 4, 5, 6]))
print(filter_events([10, 15, 20, 25]))
print(filter_events([1, 3, 5]))

def list_stats(numbers):
    if numbers:
        average = sum(numbers) / len(numbers)
        maximum = max(numbers)
        minimum = min(numbers)
        return {
            "min": min,
            "max": max,
            "avg": average
        }
    else:
        return None