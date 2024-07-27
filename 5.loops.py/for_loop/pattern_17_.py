""""
        5 
      4 4 4      
    3 3 3 3 3    
  2 2 2 2 2 2 2  
1 1 1 1 1 1 1 1 1
"""

for i in range(1, 6):
    for j in range(1, 6 - i):
        print(" ", end=" ")
    for k in range(1, 2 * i):
        print(6 - i, end=" ")
    print()
