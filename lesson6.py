age = 15
name = "John"
weight = 43.4
is_adult = True

print(f"age: {age} is {type(age)}")
print(f"weight: {weight} is {type(weight)}")
print(f"name: {name} is {type(name)}")
print(f"is adult: {is_adult} is {type(is_adult)}")

ages = []

for _ in dir(name):
    print(_)

print(hasattr(name, "upper"))
print(hasattr(name, "flight"))

print(help(str))
