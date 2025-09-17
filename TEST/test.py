# def insertion(arr):
#     n=len(arr)
#     for i in range(1,n):
#         key=arr[i]
#         j=i-1
#         while j>=0 and arr[j]>key:
#             arr[j+1]=arr[j]
#             j-=1
#         arr[j+1]=key
#     return arr
# # print(insertion([1,3,4,5,6,7,2,10,11]))






# def merge(arr1,arr2):
#     result=[]
#     i=0
#     j=0
#     while i<len(arr1) and j<len(arr2):
#         if arr1[i]<arr2[j]:
#             result.append(arr1[i])
#             i+=1
#         else:
#             result.append(arr2[j])
#     while i<len(arr1):
#         result.append(arr1[i])
#         i+=1
#     while j<len(arr2):
#         result.append(arr2[j])
#     return result

# def divide(arr):
#     if len(arr)<=1:
#         return arr
#     mid=len(arr)//2
#     left_arr=arr[0:mid]
#     right_arr=arr[mid:]

#     left_half=divide(left_arr)
#     right_half=divide(right_arr)

#     return merge(left_half,right_half)
# print(divide([1,3,4,5,6,7,2,10,11]))


class Student:
    def __init__(self,roll_no,name,age,gender, marks=[]):
        self.roll_no=roll_no
        self.name=name
        self.age=age
        self.gender=gender
        self.marks=marks

    def updateName(self, new_name):
        self.name=new_name

    def total(self):
        t=0
        for m in self.marks:
            t= t+ m
        return t
    def display(self):
        print(f"Roll No ={self.roll_no} ")
        print(f"name ={self.name} ")
        print(f"age ={self.age} ")
        print(f"Gender ={self.gender} ") 
        print(f"Marks = {self.marks}\n\n")

# s1= Student(1,"ankit",32,"male",[34,54,23,64])1


student_details= []

while True:
    print("1 add a student .")
    print("2 remove a student ")
    print("3 display all student details ")
    print("4 Update student details ")
    print("5 dispaly a student details ")
    print("6 exit ")
    choice =int(input("enter your choice ...."))
    print()
    

    if choice ==1:
        roll_no=int(input("enter roll no "))
        name=input("enter name ")
        age=int(input("enter age "))
        gender=input("enter gender5 ")
        no_of_stu=int(input("enter number of subject marks "))

        marks=[]
        for i in range(no_of_stu):
            m=int(input("enter marks = "))
            marks.append(m)
        x=Student(roll_no, name, age, gender,marks)
        student_details.append(x)
    elif choice==2:
        pass

    elif choice==3:
        if len(student_details)==0:
            print("No student Fount")

        else:
            for stu in student_details:
                stu.display()

                print("...................")
            
            
        
    elif choice==4:
        pass
    elif choice==5:
        ron=int(input("enter the no your want to search for = "))
        for stu in student_details:
            if stu.roll_no ==ron:
                stu.display()
                break
        
    elif choice==6:
        break
    
    else:
        print("invailid choice") 
        
    
