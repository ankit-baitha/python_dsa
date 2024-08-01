"""""
maximum marks
"""
from typing import List,Dict

def displayDetails(my_dict:Dict[str,List[int]]):
    maximum_marks=0
    maximum_name=""
    for key in my_dict:
        
        total=0
        for i in range(0,len(my_dict[key])):
            total=total + my_dict[key][i]
            if maximum_marks<total:
                maximum_marks=total
                maximum_name=key    
        print(f"{key} has scored {total} marks")
    print( f"name {maximum_name} marks {maximum_marks}")


details={
    "ankit":[34,53,25,75,76],
    "deepak":[64,53,45,25,76],
    "anmol":[84,53,25,75,76],
    "mustafa":[34,93,95,75,56],
    "nikhil":[34,55,45,75,76]
}
displayDetails(details)
