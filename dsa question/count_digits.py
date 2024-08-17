"""
Given a number n. Count the number of digits in n which evenly divide n. Return an integer, total number of digits of n which divides n evenly.

Note :- Evenly divides means whether n is divisible by a digit i.e. leaves a remainder 0 when divided.

"""

def evenlyDivides (N:int)->int:
        # code here
        count=0
        temp=N
        while temp>0:
            last= temp%10
            if (last !=0 and N%last==0):
                count+=1
    
            temp=temp//10
        return count
        
print(evenlyDivides(120))