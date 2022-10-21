class Microsoft:
    def __init__(self,name,product):
        self.name = name
        self.product  = product
    def get_employee(self):
        print(f"The name of the employee is {self.name} and he is working on the projet { self.product}")
    
samir = Microsoft("Samir Paul","Windows-10")
aniket = Microsoft("Aniket Mandi","One-drive")
samir.get_employee()
aniket.get_employee()
