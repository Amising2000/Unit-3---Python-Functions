# 5
18.00
18.00


# 6
def make_notification(user, *messages, urgent=False):
    full_message = ""

    for message in messages:
        full_message += message

    if urgent == True:
        return f"URGENT: {user} - {message}"
    else:
        return f"{user} - {message}"

print(
    make_notification("admin", "Server down!", urgent=True)
)  # URGENT: admin - Server down!
print(make_notification("user", "Welcome", "Check inbox"))


# 7
"""SELECT name, email FROM users"""
"""SELECT * FROM logs WHERE "level= 'error'" LIMIT 5"""


# 8
def log_action(actor, *actions, timestamp=None, **context):
    all_actions = ", ".join(actions)
    
    full_context = ""
    for k, v in context.items():
        if full_context:
            full_context += ", "
        full_context += f"{k}={v}"
    
    return f"{actor}: {all_actions} | {f'{timestamp}, ' if timestamp is not None else ''}{full_context}"

print(
    log_action("bot", "login", "scan", source="API", ip="1.2.3.4")
)  # bot: login, scan | source=API, ip=1.2.3.4
