def calculate_cart_total(*prices):
    """
    Calculate total for any number of items
    Parameter: variable number of all price values.
    Returns: total sum of all prices rounded to 2 decimals.
    """
    # check if cart is empty
    if not prices:
        return "$0.00"
    # sum all prices
    subtotal = sum(prices)
    # Round to 2 decimal and return
    return round(subtotal, 2)

print(f"Empty Cart: ${calculate_cart_total()}")
print(f"${calculate_cart_total(19.99)}")
print(f"${calculate_cart_total(19.99, 12.34, 2.99)}")
print(f"${calculate_cart_total(19.99, 4.50, 7.99, 8.65)}")


def create_order(customer_name, **items):
    """Create an order with any menu items"""
    return {
        "customer": customer_name,
        "items": items,
        "Quantity": len(items)
    }

# Different Customers
order1 = create_order("Alex", pizza = 2, soda = 1, wings = 12)
order2 = create_order("John", burger = 1, soda = 1, fries = 1, nuggets = 6)
order3 = create_order("Alice", salad = 1 )

print(f"Order 1: {order1}")
print(f"Order 2: {order2}")
print(f"Order 3: {order3}")


# Parameter order is strict
def function(required, *args, default = 0, **kwargs):
    pass