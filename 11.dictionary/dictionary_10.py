my_list=[4,5,1,3,4,4,4,7,8,8,8,5,]
# maximumm frequency how much?
# maximum frequency whose?

my_dict={}
for num in my_list:
    my_dict[num]=my_dict.get(num,0)+1
print(my_dict)

max_freq=0
max_element=0
for key in my_dict:
    if my_dict[key]>max_freq:
        max_freq=my_dict[key]
        max_element=key
print(max_element)
print(max_freq)
    