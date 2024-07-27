name = "ankit"
age = 23
gender = "male"

# method 1
# print("my name is", name)
# print("my age is", age)
# print("my gender is ", gender)
# print("my name is", name, "my age is", age, "and my gender is ", gender)

# method 2 (F-string)
# print(f"my name is {name}")
# print(f"my age is {age}")
# print(f"my gender is {gender}")
# print(f"my name is {name} my age is {age} and my gender is {gender}")

# method 3
"""
%s -> string
%d -> Integer
%f ->Float
"""
print("my name is %s" % name)
print("my age is %d" % age)
print("my gender is %s" % gender)
print("myn name is %s and age is %d, gender is %s" % (name, age, gender))


# method 4
print(f"{name = }")
print(f"{age = }")
