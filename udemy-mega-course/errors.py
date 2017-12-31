print(1)
int(9)
int(999)
print(2)
print(3)
a = [1, 2, 3]
print(a)

#runtime errors
a = 1
b = "2"
print(int(2.5))
print(a + int(b))
c = 3
#print(c/0)
def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "You are dividing by 0"
    except TypeError:
        return "Incompatible types"
    except NameError:
        return "Input is not a number"

print(divide(1, 0))
print(divide(1, 1))
print(divide(1, "hat"))
#print(divide(1, z)) still showing up as an error, not catching exception???
print("End of Program")

#error handling
def div(a, b):
    return a / b

print(div(1,0))
