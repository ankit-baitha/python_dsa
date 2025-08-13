# Write a function that takes a string and returns it reversed.
def string_reverse(my_string:str):

    revers_string=""
    n=len(my_string)
    for i in range(n-1,-1,-1):
        revers_string=revers_string + my_string[i]
    return revers_string
my_string="ankitkumar"
print(string_reverse(my_string))

