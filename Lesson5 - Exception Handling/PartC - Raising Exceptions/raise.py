# The raise syntax
# Basic syntax
'''
raise ExceotionType("Your message!")
Examples:
raise ValueError("Quantity must be at least 1")
raise TypeError("Expected a player object, got a potato")
raise PermissionError("You are not a mod")
'''

# Just returning
def open_loot_box(player, qty):
    if qty <= 0:
        return None
    # rest of the code

# Raising Exception
def open_loot_box(player, qty):
    if qty <= 0:
        raise ValueError("Bad qty")
    # rest of the code


VALID_PROTEINS = ['chicken', 'steak', 'barbacoa', 'carnitas']
VALID_RICE = ['white', 'brown', 'none']
VALID_BEANS = ['black', 'pinto', 'none']
MAX_FREE_EXTRAS = 3

def build_bowl(protein, rice, extras):
    """Build a Chipotle bowl with validation.

    Raises:
        ValueError: If protein is invalid
        TypeError: If extra is not a list
    """
    #1 check if extras is not a list
    if not isinstance(extras, list):
        raise TypeError("Extras must be a list")
    #1 validate protein
    if protein.lower() not in VALID_PROTEINS:
        raise ValueError(f"'{protein}' isn't valid! Choose from: {VALID_PROTEINS}")
    #3 return the bowl
    return{
        "protien": protein,
        "rice": rice,
        "extras": extras,
        "price": 10.50
    }

# Test the function
try:
    # bowl = build_bowl("chicken", "brown", "corn") #Error: Extras must be a list
    bowl = build_bowl("chicken", "brown", ["corn"])
    print(f"Created: {bowl}")
except Exception as e:
    print(f"Error: {e}")