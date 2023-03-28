def maxProfit(prices):
   
    desc = sorted(prices, reverse = True)
    if desc == prices:
        return 0
    lst = []
    for i in range(len(prices)):
        for ii in range(i+1, len(prices)):
            diff = prices[i]-prices[ii]
            lst.append(diff)
    print(lst)
    profit = -1*min(lst)
    print(profit)

    return profit
    
hello = [3,4,5,6,1,7]

maxProfit(hello)
