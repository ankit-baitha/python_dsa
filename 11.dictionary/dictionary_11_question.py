my_sting="fdsfdagagsaasgafsghgzzgfagagfsd"
my_dic={}
for i in my_sting:
    my_dic[i]=my_dic.get(i,0)+1
print(my_dic)

frequency=0
max_latter=0
minimum_frequency=34567 # infinit number
for key in my_dic:
    if my_dic[key]>frequency:
        frequency=my_dic[key]
        max_latter=key
    if my_dic[key]<minimum_frequency:
        minimum_frequency=my_dic[key]
        mininum_latter=key

print("maximum latter = ", max_latter)
print("maximum frequency of latter ",frequency)

print("minimum latter  ",minimum_frequency)
print("minimum frequency of ",minimum_frequency)

