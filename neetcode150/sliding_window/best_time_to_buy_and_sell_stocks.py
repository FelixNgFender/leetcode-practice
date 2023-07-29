def maxProfit(prices):
    left, right = 0, 1
    maxDiff = 0
    while right < len(prices):
        if prices[left] > prices[right]:
            left = right
        else:
            maxDiff = max(maxDiff, prices[right] - prices[left])
        right += 1
    return maxDiff


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))

prices = [7, 6, 4, 3, 1]
print(maxProfit(prices))
