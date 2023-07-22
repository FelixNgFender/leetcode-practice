import math


def minEatingSpeed(piles, h):
    def totalHours(k):
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / k)
        return hours

    if h == len(piles):
        return max(piles)

    # guaranteed len(piles) <= h:
    # solution space: (1, max(piles))
    # binary search on that range

    lo, hi = 1, max(piles)
    res = hi
    while lo <= hi:
        k = (lo + hi) // 2
        timeTaken = totalHours(k)
        if timeTaken <= h:
            res = min(res, k)
            hi = k - 1
        else:
            lo = k + 1

    return res


piles = [3, 6, 7, 11]
h = 8
print(minEatingSpeed(piles, h))

piles = [30, 11, 23, 4, 20]
h = 5
print(minEatingSpeed(piles, h))

piles = [30, 11, 23, 4, 20]
h = 6
print(minEatingSpeed(piles, h))
