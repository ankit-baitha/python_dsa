'''Q1. Ask number of subjects from the user. Ask the subject name and marks
from the user and store that into the dictionary and print it'''

# no_of_subject=int(input("Enter the number of subjects = "))
# my_dict={}
# for i in range(0,no_of_subject):
#     subject_name=input("enter the subject name = ")
#     subject_marks=int(input("Enter the subject marks = "))
#     my_dict[subject_name]=subject_marks
# print(my_dict)
# \

'''
Q2. Given a list of integers, create a dictionary that stores each unique
integer as a key and its frequency as the value. Find the integer with the
maximum frequency.
'''


my_list=[4, 5, 6, 5, 4, 4, 7]
my_dict_2={}
for num in my_list:
    my_dict_2[num]=my_dict_2.get(num,0)+1
max_frequency=max(my_dict_2.values())

max_num = max(my_dict_2, key=my_dict_2.get)
print(f" {max_num} (frequency) {max_frequency}")
