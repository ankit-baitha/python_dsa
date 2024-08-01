class Student:
    # magic/dunder method
    
    def __init__(self,idd:int,name:str,age:int,gender="") ->None:
        self.idd=idd
        self.name=name
        self.age=age
        self.gender=gender
    # def __init__(self):
    #     self.idd=int(input("enter id "))
    #     self.name=input("enter name ")
    #     self.age=int(input("enter age "))
    #     self.gender=input("enter gender ")
    def display(self):   
        print(f"id = {self.idd}")
        print(f"name = {self.name}")
        print(f"age = {self.age}")
        print(f"gender = {self.gender}")
# s1=Student()
# s2=Student()
# s1.display()
# s2.display()
s1=Student(1,"ankit",23,"male")
s1.display()
 