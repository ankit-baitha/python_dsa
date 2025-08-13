import math
def lcm_gcd(a,b):
    gcd_val=math.gcd(a,b)
    lcm_val=abs(a*b)//gcd_val
    return [lcm_val,gcd_val]
print(lcm_gcd(5,10))