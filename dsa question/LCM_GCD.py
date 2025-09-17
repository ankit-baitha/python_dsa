
'''
Given two integers a and b, You have to compute their LCM and GCD and return an array containing their LCM and GCD.

Examples:

Input: a = 5 , b = 10
Output: [10, 5]
Explanation: LCM of 5 and 10 is 10, while their GCD is 5.
Input: a = 14 , b = 8
Output: [56, 2]
Explanation: LCM of 14 and 8 is 56, while their GCD is 2.

'''
import math
def lcm_gcd(a,b):

    gcd_value = math.gcd(a,b)
    lcm_value = abs(a*b)//gcd_value
    return [lcm_value, gcd_value]
print(lcm_gcd(5,10))