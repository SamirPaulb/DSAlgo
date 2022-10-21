class Employee:
    company = "Google"
    salary = 100

harry = Employee()
rajni = Employee()
harry.salary = 300
rajni.salary = 400

print(harry.company)
print(rajni.company)
Employee.company = "YouTube"
print(harry.company)
print(rajni.company)
print(harry.salary)
print(rajni.salary)