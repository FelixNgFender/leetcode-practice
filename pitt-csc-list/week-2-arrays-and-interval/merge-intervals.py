def merge(intervals: list[int]):
    intervals.sort(key=lambda x: x[0])
    i = 1
    accum = intervals[0]
    res = []
    while i < len(intervals):
        if intervals[i][0] <= accum[1] and intervals[i][1] > accum[1]:
            accum[1] = intervals[i][1]
        elif intervals[i][0] > accum[1]:
            res.append(accum)
            accum = intervals[i]
        i += 1
    res.append(accum)
    return res


intervals = [[1, 4], [0, 4]]
print(merge(intervals))

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge(intervals))

intervals = [[1, 4], [4, 5]]
print(merge(intervals))

intervals = [[1, 4], [2, 3]]
print(merge(intervals))
