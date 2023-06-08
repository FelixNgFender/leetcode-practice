def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x: x[1])
    numRemoves = 0
    end = intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] < end:
            numRemoves += 1
        else:
            end = intervals[i][1]
    return numRemoves


intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
print(eraseOverlapIntervals(intervals))

intervals = [[1, 2], [1, 2], [1, 2]]
print(eraseOverlapIntervals(intervals))

intervals = [[1, 2], [2, 3]]
print(eraseOverlapIntervals(intervals))
