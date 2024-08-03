class Rectange:
    
    # def __init__(self,length:float,breath:float)->None:
    #     self.length=length
    #     self.breath=breath
    
    def __init__(self) -> None:
        self.length=float(input("enter the number "))
        self.breath=float(input("enter the number "))
    def area(self)->float:
        return self.length * self.breath
    def perimeter(self):
        return 2*(self.length + self.breath)
    
    def is_square(self)->bool:
        return self.length== self.breath
x=Rectange()
print(x.area())
print(x.perimeter())
print(x.is_square())