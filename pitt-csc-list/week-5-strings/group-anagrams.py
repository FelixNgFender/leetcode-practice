from collections import defaultdict


def groupAnagrams(strs):
    def generatePrimes(count):
        primes = []
        sieve = [True] * (count * 11)  # Assuming a rough estimate of the upper bound
        num = 2
        while len(primes) < count:
            if sieve[num]:
                primes.append(num)
                for i in range(num * 2, len(sieve), num):
                    sieve[i] = False
            num += 1
        return primes

    primes = generatePrimes(26)
    # Map product of primes to anagrams
    res = defaultdict(list)
    # Map primes[i] to ord(str[j]) - ord("a")
    for s in strs:
        accum = 1
        for c in s:
            accum *= primes[ord(c) - ord("a")]
        res[accum].append(s)
    return list(res.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))

strs = [""]
print(groupAnagrams(strs))

strs = ["a"]
print(groupAnagrams(strs))
