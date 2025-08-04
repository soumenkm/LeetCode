class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key=len)
        def isPred(word1: str, word2: str) -> bool:
            if len(word1) + 1 != len(word2):
                return False
            
            count = 0
            n = len(word2)
            i = 0
            j = 0
            while i < n - 1 and j < n:
                if word1[i] == word2[j]:
                    i = i + 1
                else:
                    count = count + 1
                j = j + 1

            if count <= 1:
                return True
            else:
                return False
            
        n = len(words)
        DP = [1 for i in range(n)]
        for i in range(1, n):
            for j in range(0, i):
                if isPred(words[j], words[i]):
                    DP[i] = max(DP[i], 1 + DP[j])
        return max(DP)