target_percentage = -1

# Program process that gets target integer
def get_percentage() -> int:
    while True:
        try:
            num = int(input("At what battery percentage would you like to be notified?\n"))
        except ValueError:
            input("Input could not be read as number. Press enter to continue.")
            continue
        if num < 0 or num > 100:
            input("Input is outside of the 0-100 range. Press enter to continue.")
            continue
        return num

# Main
print("Welcome to lilbatteryjr!")
print(f"Number chosen: {get_percentage()}")