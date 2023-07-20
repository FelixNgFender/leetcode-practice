from collections import defaultdict


def isAnagram(s, t):
    if len(s) != len(t):
        return False
    sChars = [0] * 26
    tChars = [0] * 26
    for c in s:
        sChars[ord(c) - ord("a")] += 1
    for c in t:
        tChars[ord(c) - ord("a")] += 1
    return sChars == tChars


def unicodeFollowUp(s, t):
    if len(s) != len(t):
        return False
    sChars = defaultdict(int)
    tChars = defaultdict(int)
    for c in s:
        sChars[c] += 1
    for c in t:
        tChars[c] += 1
    return sChars == tChars


s = "anagram"
t = "nagaram"
print(isAnagram(s, t))

s = "rat"
t = "car"
print(isAnagram(s, t))
