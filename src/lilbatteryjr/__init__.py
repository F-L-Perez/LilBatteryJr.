import psutil

# Program process that gets target integer
def get_percentage() -> int:
    while True:
        # Make sure input is integer
        try:
            num = int(input("At what battery percentage would you like to be notified?\n"))
        except ValueError:
            input("Input could not be read as number. Press enter to continue.")
            continue
        # Make sure input falls under range
        if num < 0 or num > 100:
            input("Input is outside of the 0-100 range. Press enter to continue.")
            continue
        return num

def battery():
    return psutil.sensors_battery()

# Percentage monitor process
def monitor(target):
    while True:
        b = battery()
        if b.percent == target_percent:
            print(f"ATTENTION: YOUR DEVICE HAS REACHED {b.percent}% BATTERY")
            break
        elif b.percent < target_percent:
            print(f"ATTENTION: YOUR DEVICE HAS REACHED BELOW {b.percent}% BATTERY")
            break

# Main
print("Welcome to lilbatteryjr!")
target_percent = get_percentage()
print(f"Number chosen: {target_percent}")
monitor(target_percent)