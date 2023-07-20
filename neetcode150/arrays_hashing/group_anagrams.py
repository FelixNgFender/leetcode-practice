from collections import defaultdict


def groupAnagrams(strs):
    def anagramToPrimeProduct(s):
        if s == "":
            return 0
        res = 1
        for c in s:
            res *= primes[ord(c) - ord("a")]
        return res

    primes = [
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
        83,
        89,
        97,
        101,
    ]

    productsToAnagrams = defaultdict(list)
    for s in strs:
        productsToAnagrams[anagramToPrimeProduct(s)].append(s)
    return list(productsToAnagrams.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))

strs = [""]
print(groupAnagrams(strs))

strs = ["a"]
print(groupAnagrams(strs))
