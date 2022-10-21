class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee() 

print(emp_1)  #this will print the space occupied by the instance
print(emp_2)  #this will print the space occupied by the instance

emp_1.first = 'Samir'
emp_1.last = 'Paul'
emp_1.email = 'samir.paul@gmail.com'
emp_1.pay = 5555000000000


emp_2.first = 'Corey'
emp_2.last = 'Schafer'
emp_2.email = 'corey.schafer@companey.com'
emp_2.pay = 3330000

print(emp_1.email)
print(emp_2.email)

