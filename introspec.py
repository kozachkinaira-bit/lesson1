import random

for _ in dir(random):
    print(_)

print(help(random))
print(hasattr(random, "upper"))
print(hasattr(random, "random"))