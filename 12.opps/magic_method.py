class Rectange:
    
    def __init__(self,length:float,breath:float)->None:
        self.length=length
        self.breath=breath
        
    # magic method 
    def __str__(self)->str:
        # return "my reactangle object"
        return f"{self.length} {self.breath}"
    
    def area(self)->float:
        return self.length * self.breath
    def perimeter(self):
        return 2*(self.length + self.breath)
    
    def is_square(self)->bool:
        return self.length== self.breath
x=Rectange(5,4)
print(x) # address
my_list=[3,5,6,63,2]
print(my_list) # [3,5,6,63,2]