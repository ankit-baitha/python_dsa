class Student:
    # class variable / attributes
    idd=0
    name=""
    age=-0
    gender=""
    #method 
    def setDetails(self):
        self.idd=int(input("enter id "))
        self.name=input("enter name ")
        self.age=int(input("enter age "))
        self.gender=input("enter gender ")
    def display(self):   
        print(f"id = {self.idd}")
        print(f"id = {self.name}")
        print(f"id = {self.age}")
        print(f"id = {self.age}")
s1=Student()
s2=Student()
s1.setDetails()
s1.display()
s2.setDetails()
s2.display()

