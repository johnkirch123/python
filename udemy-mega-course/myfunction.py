def minutes_to_hours(minutes):
    hours = minutes / 60
    return hours

def seconds_to_hours(seconds):
    hours = seconds / 3600
    return hours

def calculate_time(minutes, seconds=30):
    hours = minutes / 60 + seconds / 60
    return hours

#default value needs to be after first argument
print(calculate_time(300))

print(minutes_to_hours(70))
print(type(minutes_to_hours(70)))

print(seconds_to_hours(4596))
print(type(seconds_to_hours(70)))

#28 functions and user input
def age_foo(age):
    new_age = float(age) + 50
    return new_age
print(age_foo(input("Enter your age: ")))
