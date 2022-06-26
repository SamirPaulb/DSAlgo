# Python Object Oriented Programming by Joe Marini course example
# Creating immutable data classes

from dataclasses import dataclass


@dataclass()  # TODO: "The "frozen" parameter makes the class immutable
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0


obj = ImmutableClass()
print(obj.value1)

# TODO: attempting to change the value of an immutable class throws an exception


# TODO: even functions within the class can't change anything
