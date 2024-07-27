# spread , splat
 
 # *args =n3
 
def add(n1, n2, *n3):
    print(f"n1 -> {n1}")
    print(f"n1 -> {n2}")
    print(f"n1 -> {n3}")


def add_1(n1, n2, **args):
    print(f"n1 -> {n1}")
    print(f"n1 -> {n2}")
    print(f"n1 -> {args}")


def add1(n1,*n3, n2):
    print(f"n1 -> {n1}")
    print(f"n1 -> {n2}")
    print(f"n1 -> {n3}")

# **kwargs


# add(12,12,12,12,32)
add(12, 12, 12, 12, 32)
# add1(13,24,234,234,234) error

