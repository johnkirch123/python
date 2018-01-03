def cel_to_fahr(c):
    if float(c) > -273.16:
        f = float(c) * 9/5 + 32
        return f
    else:
        return "Impossible temperature."

print(cel_to_fahr(input("Please enter a temperature for conversion from C to F: ")))
