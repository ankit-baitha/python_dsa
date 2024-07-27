""""
loops 
continue (skips the below part of the code and moves ot next loop)
break (break from the loop )

"""

# i = 1
# while i <= 10:
#     print("hello")
#     i += 1
#     print("good", end=" ")
#     print("bye", end=" ")
#     print("done")

i = 1
while i <= 5:
    print("hello")
    i += 1
    if i == 2:
        continue
    print("good", end=" ")
    print("bye", end=" ")
    print("done")


# j=1
# while j<=5:
#     print("hello")
#     if  j==3:
#         continue
#     j+=1

# output 3 time hello and infinite time hello

k = 1
while k <= 5:
    print("hello")
    if k == 3:
        break
    k += 1
print("done")
# output 3 time hello and one time done


# # return out from fucntion
def A():
    k = 1
    while k <= 5:
        print("hello")
        if k == 3:
            return
        k += 1
    print("done")


A()
