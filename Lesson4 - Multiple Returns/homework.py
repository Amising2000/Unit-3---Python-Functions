# 1
def search_user_database(data):
    result = None
    message = ""
    boolean = False
    users = "john"

    if data.strip() == "":
        result = None
        message = "No search query"
        boolean = False
    elif not data.isalpha():
        result = False
        message = "Invalid characters"
        boolean = False
    elif data != users:
        result = 0
        message = "No users found"
        boolean = True
    else:
        result = 3
        message = "Found 3 users"
        boolean = True
    
    return result, message, boolean

# TEST 1: Empty string → None (no value provided)
result, message, success = search_user_database("")
print(result)  # None
print(message)  # "No search query"
print(success)  # False

# TEST 2: Whitespace only → None (no value provided)
result, message, success = search_user_database(" ")
print(result)  # None
print(message)  # "No search query"
print(success)  # False

# TEST 3: Has numbers → False (operation failed)
result, message, success = search_user_database("user123")
print(result)  # False
print(message)  # "Invalid characters"
print(success)  # False

# TEST 4: Has special chars → False (operation failed)
result, message, success = search_user_database("user@email")
print(result)  # False
print(message)  # "Invalid characters"
print(success)  # False

# TEST 5: Valid but no results → 0 (valid count of zero)
result, message, success = search_user_database("admin")
print(result)  # 0
print(message)  # "No users found"
print(success)  # True ← Search worked! Just found nothing

# TEST 6: Valid with results → positive int
result, message, success = search_user_database("john")
print(result)  # 3 (or any positive number)
print(message)  # "Found 3 users"
print(success)  # True


# 2
def analyze_book_pages(books, long_book=False):
    if not books:
        return (0, 0, 0.0, False)

    total_books = len(books)
    total_pages = sum(books)
    average_pages = round(total_pages / total_books, 2)
    for book in books:
        if book > 500:
            long_book = True
    return total_books, total_pages, average_pages, long_book

# TEST 1: Mixed collection with one long book
count, total, avg, has_long = analyze_book_pages([250, 180, 620, 310])
print(count)  # 4
print(total)  # 1360
print(avg)  # 340.0
print(has_long)  # True (because 620 > 500)

# TEST 2: No long books
count, total, avg, has_long = analyze_book_pages([200, 150, 300])
print(count)  # 3
print(total)  # 650
print(avg)  # 216.67 (approximately)
print(has_long)  # False (all books ≤ 500)

# TEST 3: Empty list - EDGE CASE!
count, total, avg, has_long = analyze_book_pages([])
print(count)  # 0
print(total)  # 0
print(avg)  # 0.0
print(has_long)  # False

# TEST 4: Exactly 500 pages - TRICKY!
count, total, avg, has_long = analyze_book_pages([500, 400, 300])
print(has_long)  # False (500 is NOT > 500)

# TEST 5: Exactly 501 pages
count, total, avg, has_long = analyze_book_pages([501, 400, 300])
print(has_long)  # True (501 IS > 500)