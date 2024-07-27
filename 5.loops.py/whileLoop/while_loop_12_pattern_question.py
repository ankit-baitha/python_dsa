def pattern(number):
    n = 1
    i = 1
    while i <= number:
        print(n)
        n = (n * 10) + 1
        i += 1


number = int(input("enter the number of rows : "))
pattern(number)
