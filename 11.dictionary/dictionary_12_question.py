"""""
ankit has scored  marks
"""
from typing import List,Dict
# method 1
def displayDetails(my_dict:Dict[str,List[int]]):
    for name,marks in my_dict.items():
        # print(f"{name} has scored {sum(marks)}")
        total=0
        for mark in marks:
            total=total+mark
        print(f"{name} has scored {total}")
        
#method 2      

def displayDetails(my_dict:Dict[str,List[int]]):
    for key in my_dict:
        total=0
        for i in range(0,len(my_dict[key])):
            total=total + my_dict[key][i]
        print(f"{key} has scored {total} marks")


details={
    "ankit":[34,53,25,75,76],
    "deepak":[64,53,45,25,76],
    "anmol":[84,53,25,75,76],
    "mustafa":[34,93,95,75,56],
    "nikhil":[34,55,45,75,76]
}
displayDetails(details)
