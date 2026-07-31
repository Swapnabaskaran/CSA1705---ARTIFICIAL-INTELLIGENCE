room = input("Enter room status (C for Clean, D for Dirty): ").upper()

if room == "D":
    print("Vacuum Cleaner: Cleaning the room...")
    room = "C"

print("Final Room Status:", room)
