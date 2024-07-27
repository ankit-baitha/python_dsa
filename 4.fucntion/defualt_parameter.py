# default parameter


# order
def marks(math=0, english=0, science=0, hindi=0, socialscience=0):
    precentage = (math + english + science + hindi + socialscience) / 5
    print(f"precentage is {precentage} %")


# requirment and optional
def into(name, age="", gender=""):
    print(name, age, gender)


marks(90, 90, 90, 90, 90)

into("ankit", 23)
