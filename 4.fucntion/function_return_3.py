def average(n1: int, n2: int, n3: int, n4: int, n5: int) -> float:  # by default None
    total = n1 + n2 + n3 + n4 + n5
    return total / 5


def concat(frist_name:str,last_name:str) ->str:
    return frist_name+last_name


x = average(34, 53, 63, 33, 53)
print(x)

