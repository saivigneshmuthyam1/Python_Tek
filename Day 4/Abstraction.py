from abc import ABC, abstractmethod
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass 
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
     def __init__(self,radius):
         self.radius=radius
     def area(self):
         print(f"Area of circle: {3.14*self.radius*self.radius}")
     def perimeter(self):
         print(f"Perimeter of circle: {2 * 3.14 * self.radius}")


class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth 
    def area(self):
        print(f"Area of rectangle: {self.length*self.breadth}") 
    def perimeter(self):
        print("Perimeter of circle:",end="")
        print(2 * (self.length + self.breadth))

circle_obj=Circle(7)
rect_obj=Rectangle(10,6)
circle_obj.area()
rect_obj.area()
circle_obj.perimeter()
rect_obj.perimeter()