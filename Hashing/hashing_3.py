
s="adfghjmgsjhvjfvbjsvghjhjdfkvcbzxvgv"
lis=['a','g','h','z','k']
d={}
for ch in s:
    d[ch]=d.get(ch,0)+1
for ch_ in lis:
    print(ch_,d.get(ch_,0))

# time complexity =O(n)*O(m)
# space complexity =O(N)