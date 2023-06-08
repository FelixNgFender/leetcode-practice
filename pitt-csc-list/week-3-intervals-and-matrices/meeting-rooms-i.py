def canAttendMeetings(intervals):
    intervals.sort(key=lambda x: x[0])
    if not intervals:
        return True
    lastEndTime = intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] < lastEndTime:
            return False
        lastEndTime = max(intervals[i][1], lastEndTime)
    return True

intervals = [(0,30),(5,10),(15,20)]
print(canAttendMeetings(intervals))

intervals = [(5,8),(9,15)]
print(canAttendMeetings(intervals))
