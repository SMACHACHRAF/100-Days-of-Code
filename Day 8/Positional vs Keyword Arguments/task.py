# Functions with input
"""
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")
"""
#Function with more than 1 input
#keynord argument
def greet_with(name="Achraf", location="Monastir"):
    print(f"Hello {name}")
    print(f"what is it like in {location}")
greet_with()
#positional argument
#greet_with("Jack", "Monastir")
#greet_with("Monastir","Jack")
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"what is it like in {location}")
greet_with(name="Achraf", location="Monastir")



