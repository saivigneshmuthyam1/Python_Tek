class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def display(self):
        print(f"Name:{self.name}\nRoll:{self.id}\n")

class Manager(employee):
    def __init__(self,department,name,id):
         super().__init__(name,id)
         self.department = department
        
    def display(self):
        print(f"Name:{self.name}\nid:{self.id}\ndepartment:{self.department}")


emp=employee("vignesh",6741)
emp.display()

print("-"*20)

mag=Manager("DS","SAI",2341)
mag.display()   




