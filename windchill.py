# James Shaw
# CSCI151
# 1/18/22
# windchill.py

import sys
import stdio

args = sys.argv[1:]
if len(args) < 2:
    temp = float(input("Input temperature in fahrenheit: "))
    wind_speed = float(input("Input wind speed (mph): "))
else:
    temp = float(args[0])
    wind_speed = float(args[1])

# Calculate wind chill
wind_chill = 35.74 + 0.6215 * temp + (
        0.4275 * temp - 35.75) * wind_speed ** 0.16

# Outputs
stdio.writeln("Temperature = {:.1f}".format(temp))
stdio.writeln("Wind speed = {:.1f}".format(wind_speed))
stdio.writeln(f"Wind chill = {wind_chill}")
