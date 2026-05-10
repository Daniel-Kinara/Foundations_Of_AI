# Vacuum Cleaner Agent

# Environment
rooms = {"A": "Dirty", "B": "Dirty"}

# Vacuum starts at room A
current_room = "A"


# Function to clean room
def clean_room(room):

    global rooms

    if rooms[room] == "Dirty":

        print(f"Room {room} is Dirty.")
        print(f"Cleaning Room {room}...")

        rooms[room] = "Clean"

    else:
        print(f"Room {room} is already Clean.")


# Clean current room
clean_room(current_room)

# Move to next room
current_room = "B"

print("\nMoving to Room B...\n")

# Clean second room
clean_room(current_room)

# Final status
print("\nFinal Room Status:")
print(rooms)
