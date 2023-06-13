from collections import defaultdict


def isAnagram(s, t):
    if len(s) != len(t):
        return False
    wordCnt1 = defaultdict(int)
    wordCnt2 = defaultdict(int)
    for c in s:
        wordCnt1[c] += 1
    for c in t:
        wordCnt2[c] += 1
    return wordCnt1 == wordCnt2


s = "anagram"
t = "nagaram"
print(isAnagram(s, t))

s = "rat"
t = "car"
print(isAnagram(s, t))
