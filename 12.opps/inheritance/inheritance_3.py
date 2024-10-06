class Animal:
    def set_animal_details(self):
        self.color=input("Enter color = ")
        self.sound=input("Enter sound = ")
        self.height=int(input("Enter height = "))
    def details(self):
        print("-----1------")
        print(f"color = {self.color}")
        print(f"sound = {self.sound}")
        print(f"height = {self.height}")
        
        
class Dog(Animal):
    def __init__(self):
        self.set_animal_details()
        self.dog_name=input("Enter dog name = ")
        self.dog_owner=input("Enter dog owner name  = ")
        
    def display(self):
        print("------2----")
        print(f"Dog name={self.dog_name}")
        print(f"Dog name={self.dog_owner}")
        print(f"Dog name={self.color}")
        print(f"Dog name={self.sound}")
        print(f"Dog name={self.height}")
        
    def details(self):
        # self.display()
        
        #super key word
        super().details()
        

        
d1=Dog()
d1.details()

