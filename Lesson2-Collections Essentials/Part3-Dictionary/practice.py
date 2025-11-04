# 2
def find_top_players(players, min_score):
    """Return a list of usernames for players with score >= min_score"""
    # YOUR CODE HERE
    highest_score = []
    for player in players:
        if player['score'] >= min_score:
            highest_score.append(player['username'])
    return highest_score

# Test it
players = [
    {"username": "DragonSlayer", "score": 8500},
    {"username": "NinjaWarrior", "score": 6200},
    {"username": "MageKing", "score": 9100},
    {"username": "ShadowAssassin", "score": 5800},
]

result = find_top_players(players, 7000)
print(result)  # Should print: ['DragonSlayer', 'MageKing']


# 3
'9'
'EYE OF THE TIGER'
'BLINDING LIGHTS'


# 4
def calculate_cart_total(cart):
    """Calculate the total cost of all items in the cart and returns: total cost (float)"""
    # YOUR CODE HERE
    total = 0
    for product in cart:
        cost = product['price'] * product['quantity']
        total += cost
    return total

# Test it
cart = [
    {"item": "Laptop", "price": 899.99, "quantity": 1},
    {"item": "Mouse", "price": 24.99, "quantity": 2},
    {"item": "Keyboard", "price": 79.99, "quantity": 1},
    {"item": "USB Cable", "price": 9.99, "quantity": 3}
]

total = calculate_cart_total(cart)
print(f"Total: ${total:.2f}")  # Should print: Total: $1059.93