# Python Object Oriented Programming by Joe Marini course example
# Creating immutable data classes

from dataclasses import dataclass


@dataclass(frozen=True)  # "The "frozen" parameter makes the class immutable
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0

    def somefunc(self, newval):
        self.value2 = newval


obj = ImmutableClass()
print(obj.value1)

# attempting to change the value of an immutable class throws an exception
obj.value1 = "Another value"
print(obj.value1)

# Frozen classes can't modify themselves either
obj.somefunc(20)
