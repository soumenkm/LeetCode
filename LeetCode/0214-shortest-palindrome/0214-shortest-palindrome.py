class Solution:
    def shortestPalindrome(self, s: str) -> str:
        m = len(s)
        revS = s[::-1]
        string = s + "#" + revS
        n = len(string)
        LPS = [0 for i in range(n)]
        i = 1
        length = 0

        while i < n:
            if string[i] == string[length]:
                length += 1
                LPS[i] = length
                i += 1
            elif length == 0:
                LPS[i] = 0
                i += 1
            else:
                length = LPS[length-1]
        
        maxLen = LPS[-1]
        palin = revS[:m-maxLen] + s
        return palin