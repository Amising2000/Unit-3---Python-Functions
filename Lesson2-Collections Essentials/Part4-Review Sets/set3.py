# 1
[23]

# 2
"NEXUS"


# 3
def match_mvp(players):
    best_player = ""
    best_ratio = 0.0
    for name, kd in players.items():
        kd_ratio = kd["kills"] / kd["deaths"]
    if kd_ratio > best_ratio:
        best_ratio = kd_ratio
    best_player = name

    return best_player


players = {
    "phoenix": {"kills": 28, "deaths": 12},
    "cipher": {"kills": 35, "deaths": 15},
    "blaze": {"kills": 22, "deaths": 18},
}

print(match_mvp(players))
