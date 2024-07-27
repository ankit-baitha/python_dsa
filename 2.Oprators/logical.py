"""
Logical Operator
 to operate on 2 or moere conditions
 
 AND 
 c1 c2 Result
 F  F  F
 F  T  F
 T  T  T
 T  F  F
  
OR 
C1 C2 Result
F  F  F
F  T  T
T  T  T
T  F  T
 
NOT 
Reverse the result
"""

a = 234
b = 34
print(a > b and b > a)
print(a > b or a < b)
print(not (a > b and a < b))
