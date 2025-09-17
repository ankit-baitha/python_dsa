# from typing import List
# class Student:
#     def __init__(self, roll_no, name, age, gender, marks=[]):
#         self.roll_no = roll_no
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.marks = marks 

#     # def updateName(self, new_name):
#     #     self.name = new_name

#     def total(self):
#         t = 0
#         for m in self.marks:
#             t += m
#         return t
#     def updateDetails(self, new_name=None, age=None,gender=None)->None:
#         if new_name:
#             self.name=new_name
#         if age:
#             self.age=age
#         if gender:
#             self.gender=gender
#     def dispaly(self):
#         print(f"Roll No ={self.roll_no} ")
#         print(f"name ={self.name} ")
#         print(f"age ={self.age} ")
#         print(f"Gender ={self.gender} ") 
#         print(f"Marks = {self.marks}\n\n")

    

# # s1 = Student(1, "ankit", 32, "male", [34, 54, 23, 64])
# # print(s1.total())
# student_details :List[Student]=[]
# while True:
#     print("1 add a student .")
#     print("2 remove a student ")
#     print("3 display all student details ")
#     print("4 Update student details ")
#     print("5 dispaly a student details ")
#     print("6 exit ")
#     choice=int(input("enter your choice = "))
#     print()
#     if choice==1:
#         roll_no=int(input("enter roll no : "))
#         name=input("enter name : ")
#         age=int(input("enter age : "))
#         gender= input("enter gender : ")
#         no_of_stu=int(input("enter number of subject marks "))
#         marks=[]
#         for _ in range(no_of_stu):
#             m=int(input("enter marks : "))
#             marks.append(m)
#         x=Student(roll_no,name,age,gender,marks)
#         student_details.append(x)
#     elif choice==2:
#         rno=int(input("enter the no your want to update details = "))
#         student_index=-1
#         for i in range(0,len(student_details)):
#             if student_details[i].roll_no==rno:
#                 student_index=i
#                 break
#         if student_index==-1:
#             print("Student no fount ")
#         else:
#             student_details.pop(student_index)
        
#     elif choice==3:
#         if len(student_details)==0:
#             print("No student fount ")
#         else:
#             for stu in student_details:
#                 stu.dispaly
#                 print("...........")
            
#     elif choice==4:
#         rno=int(input("enter the no your want to update details = "))
#         for stu in student_details:
#             if stu.roll_no==rno:
#                 n_name=input("enter new name")
#                 n_age=int(input("enter new name"))
#                 n_gender=input("enter new name")
#                 stu.updateDetails(n_name,n_age,n_gender)
#                 break
#     elif choice==5:
#         rno=int(input("enter the no your want to search for = "))
#         for stu in student_details:
#             if stu.roll_no==rno:
#                 stu.display()
#                 break
            

#     elif choice==6:
#         pass
#     else:
#         print("invailed choice..")
