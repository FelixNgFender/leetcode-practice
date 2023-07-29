def lengthOfLongestSubstring(s):
    seenChars = set()
    maxLength = 0
    left = 0
    for right in range(len(s)):
        if s[right] in seenChars:
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    break
                seenChars.remove(s[left])
                left += 1
        else:
            seenChars.add(s[right])
            maxLength = max(maxLength, right - left + 1)
    return maxLength


s = "abcabcbb"
print(lengthOfLongestSubstring(s))

s = "bbbbb"
print(lengthOfLongestSubstring(s))

s = "pwwkew"
print(lengthOfLongestSubstring(s))
