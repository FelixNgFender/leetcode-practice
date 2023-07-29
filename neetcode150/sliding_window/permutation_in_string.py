def checkInclusion(s1, s2):
    def includes(count1, count2):
        for key, val in count2.items():
            if not count1.get(key, True) or count1[key] < val:
                return False
        return True

    if len(s1) > len(s2):
        return False

    count1, count2 = {}, {}
    for c in s1:
        count1[c] = 1 + count1.get(c, 0)
    left = 0
    for right in range(len(s2)):
        if s2[right] not in count1:
            count2.clear()
            left = right + 1
            continue
        count2[s2[right]] = 1 + count2.get(s2[right], 0)
        if count2 == count1:
            return True
        elif includes(count1, count2):
            continue
        else:
            # count2 has a more frequent value than count1
            while left < right and not includes(count1, count2):
                count2[s2[left]] -= 1
                if count2[s2[left]] == 0:
                    count2.pop(s2[left])
                left += 1
    return False


s1 = "ab"
s2 = "eidbaooo"
print(checkInclusion(s1, s2))

s1 = "ab"
s2 = "eidboaoo"
print(checkInclusion(s1, s2))

s1 = "hello"
s2 = "ooolleoooleh"
print(checkInclusion(s1, s2))

s1 = "adc"
s2 = "dcda"
print(checkInclusion(s1, s2))
