import sys
import psutil

battery = psutil.sensors_battery() 
## pluggedIn = battery.power_plugged()
powPercent = str(battery.percent)
## isPluggedIn = if pluggedIn else 
## pcTemp = psutil.sensors_temperatures()

print("Battery: " + powPercent + " %")
