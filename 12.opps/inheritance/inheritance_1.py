class Animal:
    def set_animal_details(self):
        self.color=input("Enter color = ")
        self.sound=input("Enter sound = ")
        self.height=int(input("Enter height = "))
class Dog(Animal):
    def set_details(self):
        self.dog_name=input("Enter dog name = ")
        self.dog_owner=input("Enter dog owner name  = ")
        
    def display(self):
        print(f"Dog name={self.dog_name}")
        print(f"Dog name={self.dog_owner}")
        print(f"Dog name={self.color}")
        print(f"Dog name={self.sound}")
        print(f"Dog name={self.height}")
        

        
d1=Dog()
d1.set_animal_details()
d1.set_details()
d1.display()
