def insert(intervals, newInterval):
    lo, hi = 0, len(intervals) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if intervals[mid][0] > newInterval[0]:
            hi = mid - 1
        else:
            lo = mid + 1
    intervals.insert(lo, newInterval)
    accum = intervals[0]
    res = []
    i = 1
    while i < len(intervals):
        if intervals[i][0] <= accum[1] and intervals[i][1] > accum[1]:
            accum[1] = intervals[i][1]
        elif intervals[i][0] > accum[1]:
            res.append(accum)
            accum = intervals[i]
        i += 1
    res.append(accum)
    return res

intervals = [[1,3],[6,9]]
newInterval = [2, 5]
print(insert(intervals, newInterval))

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(insert(intervals, newInterval))
