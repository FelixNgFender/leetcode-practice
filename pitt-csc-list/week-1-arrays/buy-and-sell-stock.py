def maxProfit(prices):
    maxDiff = 0
    l, r = 0, 1
    while r < len(prices):
        currDiff =  prices[r] - prices[l]
        if currDiff > 0:
            if currDiff > maxDiff:
                maxDiff = currDiff
            r += 1
        else:
            l = r
            r += 1
    return maxDiff

prices = [7,1,5,3,6,4]
print(maxProfit(prices))

prices = [7,6,4,3,1]
print(maxProfit(prices))