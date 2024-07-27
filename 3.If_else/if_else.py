# num = int(input("enter the numebr = "))
# if num % 2 == 0 and num % 3 == 0:
#     print("yes")
# else:
#     print("no")


# age = int(input("enter the number = "))
# if age >= 18:
#     print("adult")
# elif age >= 13 and age <= 18:
#     print("teenager")
# else:
#     print("child")

"""
ask a number from  user:
num is divisible by 3 -> fod
num is divisible by 5 -> bar
num is divisible by 3 and 5 -> forbar
else 
-> invalid
"""
num = int(input("enter number = "))
if num % 3 == 0 and num % 5 == 0:
    print("forbar")
elif num % 3 == 0:
    print("for")
elif num % 5 == 0:
    print("bar")
else:
    print("invalid")
