details = {
    "ankit": {
        "age": 23, 
        "gender": "male", 
        "adult": True, 
        "marks": [3, 4, 5, 6, 2]
        },
    "nikhil": {
        "age": 26,
        "gender": "male",
        "adult": True, 
        "marks": [4, 4, 7, 2]
        },
    "mustafa": {
        "age": 13,
        "gender": "male",
        "adult": True, 
        "marks": [5, 7, 8, 3]
        },
    "rahul": {
        "age": 25,
        "gender": "male", 
        "adult": True,
        "marks": [6, 7, 4, 7]
        },
}
# print(details["ankit"]["gender"])
# # print(details["ankit"]["marks"][-1])

#method 1
for name ,info in details.items():
    if info["adult"] ==True:
        print(name,info["age"])
        print(info["marks"])
        
        
#method 2
for name, info in details.items():
    total = 0
    for i in info["marks"]:
        total = total + i
    print(f"{name} has scored {total} marks")
    
    
#method 3

for key in details:
    total=0
    for mark in details[key]["marks"]:
        total=total+ mark
    print(f"{key} has scored {total} marks")
