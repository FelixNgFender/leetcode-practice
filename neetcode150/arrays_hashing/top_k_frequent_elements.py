import heapq
from collections import defaultdict


def topKFrequent(nums, k):
    topGHeap = []
    nums.sort()
    prev = None
    count = 0
    for n in nums:
        if n == prev:
            count += 1
        elif prev == None:
            prev = n
            count = 1
        else:
            # min-heap by default, so we insert the negative
            heapq.heappush(topGHeap, (-1 * count, prev))
            prev = n
            count = 1
    # account for the last (count, prev) pair
    heapq.heappush(topGHeap, (-1 * count, prev))
    res = []
    for _ in range(k):
        res.append(heapq.heappop(topGHeap)[1])
    return res


def topKFrequentArray(nums, k):
    freq = defaultdict(int)
    buckets = [[] for _ in range(len(nums) + 1)]
    for n in nums:
        freq[n] += 1
    for n, count in freq.items():
        buckets[count].append(n)
    res = []
    for i in range(len(buckets) - 1, 0, -1):
        for val in buckets[i]:
            res.append(val)
            if len(res) == k:
                return res


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(topKFrequentArray(nums, k))

nums = [1]
k = 1
print(topKFrequentArray(nums, k))
