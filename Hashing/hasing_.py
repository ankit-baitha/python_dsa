# hashing by list
# value 0 to 13
def hashing_lst(num,m):
    hash_list=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in num:
        hash_list[i]+=1

    for n in m:
        print(hash_list[n])
num=[1,2,3,4,5,6,2,2,5,6,11,12,13,12,1,2,12]
m=[1,2,4,6,11]
hashing_lst(num,m)

