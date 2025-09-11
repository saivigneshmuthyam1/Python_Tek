class students:
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks

    def display(self):
        print(f"Name:{self.name}\nRoll:{self.roll}\nMarks:{self.marks}")

stu=students("saivignesh",6741,90)
stu.display()

