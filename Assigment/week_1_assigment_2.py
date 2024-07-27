"""Q1. Write a program that takes two numbers as input and checks if the first
number is divisible by the second.
"""

# num = int(input("enter the number 1st  : "))
# num2 = int(input("enter the number 2nd : "))
# if num % num2 == 0:
#     print("divisible by second number ")
# else:
#     print("not divisible by second number ")
"""
Q2. A student will not be allowed to sit in exam if his/her attendance is less
than 75%.
Take following input from user

Number of classes held
Number of classes attended.

1. Print percentage of class attended
2. Print Is student is allowed to sit in exam or not
"""
# attended = int(input("enter the perecentage of  classes : "))
# if attended <= 75:
#     print("not  allowed to sit in exam ", attended)
# else:
#     print("allowed to sit in exam ", attended)


""""
Q3. Write a program to check if number is divisible by 2 and 3 but not 8.
"""
# number = int(input("enter the number "))
# if number % 2 == 0 and number % 3 == 0 and number % 8 != 0:
#     print("divisible by 2 and 3 but not 8 = ", number)
# else:
#     print("divisible by 2 , 3 and 8 = ", number)

"""
Q4. Write a Python program that takes a student's score as input and
prints the corresponding grade. Use the following grading scale:
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: Below 60
"""

# score = int(input("enter the score : "))
# if score >= 90 and score <= 100:
#     print("grade A")
# elif score >= 80 and score <= 89:
#     print("grade B")
# elif score >= 70 and score <= 79:
#     print("grade C")
# elif score >= 60 and score <= 69:
#     print("grade D")
# else:
#     print("fail ")


"""
Q5. Write a program to calculate bill. Ask the final amount from the user.
You have to give discount and print the final bill after discount.
50000 above - 30% discount
40000 - 49999 - 25% discount
30000 - 39999 - 20% discount
10000 - 29999 - 10% discount
1 - 9999 - No discount
Print the discount and the final amount to be paid.
Example 1
Enter bill amount = 8000
You got 30% discount
Your final bill is Rs. 5600"""


# def discount(num: int):
#     if num >= 5000 and 9999 > num:
#         dic = (num / 100) * 30
#         total = num - dic
#         print("your get 30% dicount  ", dic)
#         print("your final bill is Rs : ", total)
#     elif num <= 4999:
#         dic = (num / 100) * 25
#         total = num - dic
#         print("your get 25% dicount  ", dic)
#         print("your final bill is Rs : ", total)
#     elif num < 3999:
#         dic = (num / 100) * 20
#         total = num - dic
#         print("your get 20% dicount  ", dic)
#         print("your final bill is Rs : ", total)
#     elif num <= 2999:
#         dic = (num / 100) * 10
#         total = num - dic
#         print("your get 10% dicount  ", dic)
#         print("your final bill is Rs : ", total)

#     if num >= 9999:
#         print("no discount")


# num = int(input("enter bill amount "))
# discount(num)


"""
Q6. Ask 4 numbers from user. Make sure all the numbers entered by user
are different. Print which number is the smallest.
"""
# a = int(input("enter the number 1: "))
# a2 = int(input("enter the number 2: "))
# a3 = int(input("enter the number 3: "))
# a4 = int(input("enter the number 4: "))
# if a < a2 and a < a3 and a < a4:
#     print("smaller number ", a)
# elif a2 < a and 2 < a3 and a2 < a4:
#     print("smaller number ", a2)
# elif a3 < a and a3 < a2 and a3 < a4:

#     print("smaller number ", a3)
# else:
#     print("smaller number ", a4)


"""
Q7. Take Salary as input from User and Update the salary of an employee.
salary less than 10,000, 5 % increment
salary between 10,000 and 20, 000, 10 % increment
salary between 20,000 and 50,000, 15 % increment
salary more than 50,000, 20 % increment
"""

# employee_salary = int(input("enter the employee salary : "))
# if employee_salary >= 50000:
#     print("current salary ", employee_salary)
#     increment = (employee_salary / 100) * 20
#     employee_salary = employee_salary + increment
#     print("20 % icreament salary ", increment)
#     print("total salary ", employee_salary)
# elif employee_salary >= 20000 and employee_salary < 50000:
#     print("current salary ", employee_salary)
#     increment = (employee_salary / 100) * 15
#     employee_salary = employee_salary + increment
#     print("15 % icreament salary ", increment)
#     print("total salary ", employee_salary)

# elif employee_salary >= 10000 and employee_salary < 20000:
#     print("current salary ", employee_salary)
#     increment = (employee_salary / 100) * 10
#     employee_salary = employee_salary + increment
#     print("15 % icreament salary ", increment)
#     print("total salary ", employee_salary)
# elif employee_salary <= 10000:
#     print("current salary ", employee_salary)
#     increment = (employee_salary / 100) * 5
#     employee_salary = employee_salary + increment
#     print("15 % icreament salary ", increment)
#     print("total salary ", employee_salary)
# else:
#     print("invalid input ")


""""
Q8. An extra day is
dded to the calendar almost every four years as
February 29, and the day is called a leap day. A leap year contains a leap
day

These are the conditions used to identify leap years:

    .if the year can be evenly divided by 4, it is then a leap year
    .but if the year is evenly divided by 4 and also by 100, then it is NOT a
     leap year

     .but if the year is evenly divided by 4 and also by 400, then it is a leap
      year
      
This means the years 2000 and 2400 are leap years, while 1800, 1900,
2100, 2200, 2300 and 2500 are NOT leap years.
Ask a year input from user. And tell if the year entered by user is leap or
not.

"""

year = int(input("Enter a year = "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
