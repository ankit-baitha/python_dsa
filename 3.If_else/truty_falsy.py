# True and False
# type casting(Impicit and explicit)
""""
int 
1,3,5,-7,1000 ->Truthy
0 ->falsy

float
1.1,4.54 -9,7,100,0.00003 ->truthy
0.0 -> falsy

srt 
"abc" ,"1244", " " ,"."  ->true
"" -> fasly

"""
a=int("100")# explicit
print(type(a))

age=34
if 88:
    print("adult")
else:
    print("child")
    
name="ankit" # truthy
if name :
    print("yes")
else:
    print("no")
    
    
name=" " # truthy
if name :
    print("yes")
else:
    print("no")

    
name="" # falsy
if name :
    print("yes")
else:
    print("no")