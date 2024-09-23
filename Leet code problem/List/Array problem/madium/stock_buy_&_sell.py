'''
brute solution 
time complexity=0(n^2)
space complexity = O(1)
'''
prices=[7,1,5,3,6,4]
n=len(prices)
max_profit =0
for i in range(0,n): #  i=1
    for j in range(i+1,n):  # j=6
        if prices[j]> prices[i]: # prfit= 6-1
            profit=prices[j]-prices[i]  # 5
            max_profit=max(max_profit,profit)   # 5
    
print(max_profit)
            

'''

'''
def stock_buy(prices):
    max_profit=0
    min_prices=float("inf")
    for i in range(0,len(prices)):
        min_prices= min(min_prices,prices[i])
        max_profit=max(max_profit,prices[i]-min_prices)
    return max_profit
prices=[7,1,5,3,6,4]
result=stock_buy(prices)
print(result)
