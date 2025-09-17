'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 
'''

def reverse_integer(num)->int:
    reverse_no=0
    is_negative = False

    if num<0:
        is_negative= True
        num =abs(num)

    while num >0:
        digit =num % 10
        reverse_no  = (reverse_no *10)+digit
        num = num //10
    if is_negative:
        reverse_no = reverse_no *-1
    if reverse_no < (-(2**31)) or reverse_no > (2**31 - 1):
            return 0
    return reverse_no
print(reverse_integer(-124))