def minWindow(s, t):
    def includes(count1, count2):
        # See if count1 is a subset of count2
        for key, val in count1.items():
            if not count2.get(key, False) or count2[key] < val:
                return False
        return True

    m, n = len(s), len(t)
    if n > m:
        return ""
    minStr, minStrLen = "", float("inf")
    res = [None, None]
    count1, count2 = {}, {}
    for c in t:
        count2[c] = 1 + count2.get(c, 0)
    left = 0
    for right in range(m):
        rightChar = s[right]
        count1[rightChar] = 1 + count1.get(rightChar, 0)
        if rightChar in count2 and includes(count2, count1):
            while left < right:
                # try to shrink left end, backtrack 1 time
                # if window invalid
                leftChar = s[left]
                count1[leftChar] -= 1
                if count1[leftChar] == 0:
                    count1.pop(leftChar)
                left += 1
                if not includes(count2, count1):
                    left -= 1
                    count1[leftChar] = 1 + count1.get(leftChar, 0)
                    break
            if right - left + 1 < minStrLen or minStr == "":
                minStr = "found one"
                minStrLen = right - left + 1
                res = [left, right]
    if res[0] != None:
        l, r = res
        minStr = s[l : r + 1]
    return minStr


s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))

s = "a"
t = "a"
print(minWindow(s, t))

s = "a"
t = "aa"
print(minWindow(s, t))

s = "acbbaca"
t = "aba"
print(minWindow(s, t))
