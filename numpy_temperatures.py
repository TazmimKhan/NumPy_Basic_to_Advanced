import numpy as np

# Daily temperatures for one week, measured in degrees Celsius.
days = np.array(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
celsius = np.array([28, 30, 32, 29, 31, 33, 27])

# NumPy converts every temperature in the array at once.
fahrenheit = celsius * 9 / 5 + 32

for day, temp_c, temp_f in zip(days, celsius, fahrenheit):
    print(f"{day}: {temp_c} C = {temp_f:.1f} F")

print(f"\nWeekly average: {np.mean(celsius):.2f} C")
print("Hottest day:", days[np.argmax(celsius)])
print("Coldest day:", days[np.argmin(celsius)])
print("Days above 30 C:", days[celsius > 30])
