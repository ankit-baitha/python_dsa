""""
keep on asking characters from the user.
stop it unitil he/she presses q

"""

my_sting = " "

while True:
    ch = input("Enter the characters = ")
    if ch == "q" or ch == "Q":
        break
    my_sting += ch
print(my_sting)
