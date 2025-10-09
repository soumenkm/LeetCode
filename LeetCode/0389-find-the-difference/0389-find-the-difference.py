class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashMap = defaultdict(int)
        for char in t:
            hashMap[char] += 1
        for char in s:
            hashMap[char] -= 1
        for k, v in hashMap.items():
            if v == 1:
                return k
