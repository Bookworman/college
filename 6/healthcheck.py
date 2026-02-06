print("Health diagnosis")
temp = float(input("Input temperature in celsium: "))
pressure = int(input("Input blood pressure in hPa: "))
pulse = int(input("Input pulse in bpm: "))

if temp > 38 or temp < 35 or pressure > 140 or pressure < 105 or pulse > 110 or pulse < 55:
    print("CALL AN AMBULANCE, CALL AN AMBULANCE (but not for me)")
elif 35 < temp < 36 or 37 < temp < 38 or 105 <= pressure <= 110 or 130 <= pressure <= 140 or 55 <= pulse <= 60 or 100 <= pulse <= 110:
    print("You'll live")
else:
    print("Go touch some grass, idc, pretty normsl")