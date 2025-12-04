# Scope - The visibillity of variables, where it can be seen, and used
# Global - outside all functions (visible everywhere)
# Local - inside a fucntion (only visable there)

# The bugs - crashes (UnboundLocalError)
def add_bonus():
    score = score + 100

score = 500
add_bonus()