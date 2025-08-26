# hashing 
# x=[2,2,4,5,5,6,5,6,7]
# def count_fre(num):
#     cnt=0
#     for i in range(0,len(x)):
#         if num==x[i]:
#             cnt +=1
#     return cnt
# print(count_fre(1))

#Hashing  ->  prestoring / fetching
def count_fre(num,num_2):
    d={}
    for i in num:
        d[i]=d.get(i,0)+1 
    for n in num_2:
        print(d[n])

num=[2,2,4,5,5,6,5,6,7]
num_2=[2,4,5,6,7]
count_fre(num,num_2)

# tc = O(n+m)
#sc=O(m)