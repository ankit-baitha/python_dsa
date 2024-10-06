class Father:
    def __init__(self) -> None:
        print("Father init ")
        self.father_name=input("Enter father name : ")
        
class Mother:
    def __init__(self) -> None:
        print("Mother init ")
        self.mother_name=input("enter mother name : ")
class son(Father,Mother):
    def __init__(self) -> None:
        Father.__init__(self)
        Mother.__init__(self)
        print("son init")
        self.name=input("enter name : ")
    def display(self):
        print(f"Father name: {self.father_name}")
        print(f"Mother name: {self.mother_name}")
        print(f"name: {self.name}")
        
        
s1=son()
s1.display()