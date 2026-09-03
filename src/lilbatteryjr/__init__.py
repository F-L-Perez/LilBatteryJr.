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
        # Make sure input batter
        return num

def battery():
    return psutil.sensors_battery()

# Percentage monitor process
def monitor(rising):
    while True:
        b = battery()

        if b.percent == target_percent:
            print(f"ATTENTION: YOUR DEVICE HAS REACHED {b.percent}% BATTERY")
            break
        elif b.percent < target_percent and not rising:
            print(f"ATTENTION: YOUR DEVICE HAS REACHED BELOW {b.percent}% BATTERY")
            break
        elif b.percent > target_percent and rising:
            print(f"ATTENTION: YOUR DEVICE HAS REACHED ABOVE {b.percent}% BATTERY")

print("Welcome to lilbatteryjr!")
target_percent = get_percentage()
print(f"Number chosen: {target_percent}")

# Get percentage and check if the system is rising or falling to the percentage
current_percent = battery().percent
if target_percent < current_percent:
    print(f"Your system will be alerted when the battery depletes to or below {target_percent}%.")
elif target_percent > current_percent:
    print(f"Your system will be alerted when the battery charges to or above {target_percent}%.")
else:
    print(f"Your system's battery is already at this percentage. Ending program.")
    quit()
rising = target_percent > current_percent

# Event loop
monitor(rising)