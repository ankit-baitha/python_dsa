class Student:
    def __init__(
        self, roll_no: int, name: str, age: int, gender: str, marks=[]) -> None:
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.gender = gender
        self.marks = marks

    def total(self) -> int:
        t = 0
        for i in self.marks:
            t = t + i
        return t

    def updateDeatails(self, new_name=None, age=None, gender=None) -> None:
        if new_name:
            self.name = new_name
        if age:
            self.age = age
        if gender:
            self.gender = gender

    def display(self):
        print(f"roll_no = {self.roll_no}")
        print(f"name = {self.name}")
        print(f"age = {self.age}")
        print(f"age = {self.age}")
        print(f"marks = {self.marks}\n \n")


student_deatails = []
while True:
    print("1) add a student ")
    print("2) remove a student")
    print("3) display student details")
    print("4)  update student details  ")
    print("5)  dispalt a student details ")
    print("6)  exit")
    choice = int(input("Enter your choice = "))
    if choice == 1:
        roll_no = int(input("enter roll no = "))
        name = input("enter your name = ")
        age = int(input("enter your age = "))
        gender = input("enter you gender = ")
        no_of_s = int(input("enter number of subject = "))
        marks = []
        for i in range(no_of_s):
            m = int(input("enter marks = "))
            marks.append(m)

        x = Student(roll_no, name, age, gender, marks)
        student_deatails.append(x)
    elif choice == 2:
        rno=int(input("enter student roll number you want to detete = "))
        student_index=-1
        for i in range(0,len(student_deatails)):
            if student_deatails[i].roll_no==rno:
                student_index=i
                break
        if student_index==-1:
            print("student not found ")
        else:
            student_deatails.pop(student_index)
                
    elif choice == 3:
        # print(student_deatails) print address
        if len(student_deatails) == 0:
            print("no student found")
        else:
            for student_object in student_deatails:
                student_object.display()
    elif choice == 4:
        rno = int(input("enter the student roll number you want to update details = "))
        for stu in student_deatails:
            if stu.roll_no == rno:
                n_name = input("enter the name = ")
                n_age = int(input("enter new  age = "))
                n_gender = input("enter new gender = ")
                stu.updateDeatails(n_name, n_age, n_gender)
                break

    elif choice == 5:
        ro_no = int(input("enter the roll number "))
        for stu in student_deatails:
            if stu.roll_no == ro_no:
                stu.dispaly()
                break
        else:
            print("no student found with roll number ")
    elif choice == 6:
        break
    else:
        print("invailad choice")
        
