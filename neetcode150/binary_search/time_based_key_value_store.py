from collections import defaultdict


class TimeMap(object):
    def __init__(self):
        # str - list[tuples]
        self.store = defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        # all input timestamps are strictly increasing
        self.store[key].append((value, timestamp))

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        res = ""
        # return empty list by default if key not found
        values = self.store.get(key, [])
        lo, hi = 0, len(values) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                lo = mid + 1
            else:
                hi = mid - 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
