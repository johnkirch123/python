def celsius_to_farenheit(c):
    if c > -273.15:
        return c * 9/5 + 32
    else:
        return "Impossible temperature."
#print(celsius_to_farenheit(float(input("Enter Celsius for conversion: "))))
temperatures=[10, -20, -289, 100]
for temp in temperatures:
    print(celsius_to_farenheit(temp))
