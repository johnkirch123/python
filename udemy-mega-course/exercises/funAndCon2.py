def string_length(mystring):
    try:
        int(mystring)
        return "Sorry integers don't have length"
    except ValueError:
        try:
            float(mystring)
            return "Sorry floats don't have length"
        except ValueError:
            return len(mystring)


print(string_length(input("Enter a word to return its length: ")))
