class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordDict = set(wordDict)
        DP = [-1 for i in range(n+1)]
        def func(index: int) -> bool:
            if DP[index] != -1:
                return DP[index]

            if index == n:
                DP[index] = True
                return True
            
            for i in range(index, n):
                seg = s[index:i+1]
                if seg in wordDict:
                    intRes = func(i+1)
                    if intRes:
                        DP[index] = True
                        return True
            DP[index] = False
            return False
        
        return func(0)