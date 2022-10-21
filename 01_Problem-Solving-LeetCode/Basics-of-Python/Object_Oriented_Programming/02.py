class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'


emp_1 = Employee('samir','paul',50000000000000000)
emp_2 = Employee('corey','schafer',1000000)


print(emp_1.email)
print(emp_2.email)
