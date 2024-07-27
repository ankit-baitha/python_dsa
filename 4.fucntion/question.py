""""
Make a function which as a integer parameter as a subject return True if pass
else False

"""


def marks(s1, s2, s3, s4, s5) -> bool:
    total = s1 + s2 + s3 + s4 + s5
    perecentage = (total / 5) * 100
    if perecentage >= 33:
        return True
    else:
        return False


x = marks(12, 23, 43, 43, 34)
print(x)
