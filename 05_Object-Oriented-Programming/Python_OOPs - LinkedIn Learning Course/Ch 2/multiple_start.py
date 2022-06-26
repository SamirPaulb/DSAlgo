# Python Object Oriented Programming by Joe Marini course example
# Understanding multiple inheritance


class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"


class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"


class C(A, B):
    def __init__(self):
        super().__init__()


c = C()
