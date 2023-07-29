def characterReplacementNeetcode(s, k):
    count = {}
    res = 0

    left = 0
    maxf = 0
    for right in range(len(s)):
        count[s[right]] = 1 + count.get(s[right], 0)
        maxf = max(maxf, count[s[right]])
        while (right - left + 1) - maxf > k:
            count[s[left]] -= 1
            left += 1

        res = max(res, right - left + 1)
    return res


def characterReplacement(s, k):
    def isValidWindow(left, right, maxFreq):
        return (right - left + 1) - maxFreq <= k

    freq = [0] * 26
    maxFreq = 0
    maxLength = 0
    left = 0
    for right in range(len(s)):
        freq[ord(s[right]) - ord("A")] += 1
        maxFreq = max(maxFreq, freq[ord(s[right]) - ord("A")])
        if isValidWindow(left, right, maxFreq):
            maxLength = max(maxLength, right - left + 1)
        else:
            while left < right and not isValidWindow(left, right, maxFreq):
                freq[ord(s[left]) - ord("A")] -= 1
                left += 1
    return maxLength


s = "ABAB"
k = 2
print(characterReplacement(s, k))

s = "AABABBA"
k = 1
print(characterReplacement(s, k))


s = "AAAA"
k = 2
print(characterReplacement(s, k))

s = "AAAB"
k = 0
print(characterReplacement(s, k))
