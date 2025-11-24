try:
    # try something risky
    score = int(input("Enter score: "))
except ValueError:
    # Runs if it FAILED
    print("Invalid score")
else:
    # Runs if it succeed
    print(f"Valid score entered: {score}")


def parse_command(message):
    """Parse a Discord command like: !ban PlayerName 7days"""
    try:
        parts = message.split()
        command = parts[0]
        target = parts[1]
        duration = parts[2]
    except IndexError:
        print("❌ Invalid command format - missing parts!")
    else:
        print("✅ Command parsed successfully!")
        if command.startswith("!"):
            print(f"⚡Executing: {command}")
        return command, target, duration
    finally: # Runs no matter what
        print("This block runs regardless")

print(parse_command("!ban PlayerName 7days"))
print(parse_command("!ban"))