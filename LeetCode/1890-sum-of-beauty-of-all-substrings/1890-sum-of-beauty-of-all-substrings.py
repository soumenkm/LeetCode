class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        beauty = 0
        for i in range(n):
            mapArr = [0 for i in range(26)]
            for j in range(i, n):
                charIdx = ord(s[j]) - ord("a")
                mapArr[charIdx] += 1
                maxFreq = max([i for i in mapArr if i > 0])
                minFreq = min([i for i in mapArr if i > 0])
                beauty += maxFreq - minFreq
        
        return beauty