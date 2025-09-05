class Solution:
    def frequencySort(self, s: str) -> str:
        hashMap = defaultdict(int)
        for char in s:
            hashMap[char] += 1
        hashMap = list(zip(hashMap.keys(), hashMap.values()))
        hashMap = sorted(hashMap, key=lambda item: item[1], reverse=True)

        res = []
        for char, count in hashMap:
            res.extend([char]*count)
        
        return "".join(res)
