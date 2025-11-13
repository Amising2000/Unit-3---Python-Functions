# 1
2300

# 2
"WOW WOW LFG"


# 3
def find_top_donor(donations):
    highest_donation = 0
    highest_donor = ''
    for donor, num in donations.items():
        if num > highest_donation:
            highest_donation = num
            highest_donor = donor
    return highest_donor

donations = {
    "neon": 250,
    "vibe": 180,
    "lunar": 400,
    "pixel": 150
}

print(find_top_donor(donations))