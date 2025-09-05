class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        length = 0
        i = 1
        LPS = [0 for i in range(n)]
        while i < n:
            if s[i] == s[length]:
                length += 1
                LPS[i] = length
                i += 1
            elif length == 0:
                LPS[i] = 0
                i += 1
            else:
                length = LPS[length-1]
        
        length = LPS[-1]
        return s[:length]