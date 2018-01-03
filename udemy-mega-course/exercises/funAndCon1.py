def string_length(mystring):
    try:
        float(mystring)
        return "Sorry integers don't have length"
    except ValueError:
        return len(mystring)


print(string_length(input("Enter a word to return its length: ")))
