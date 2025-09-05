class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        i = 0
        res = 0
        string = ""
        while i < n:
            maxOddLen = 0
            j = 0
            while 0 <= (i-j) <= (i+j) <= n-1 and s[i-j] == s[i+j]:
                maxOddLen = (2*j+1)
                if maxOddLen > res:
                    string = s[i-j:i+j+1]
                    res = maxOddLen
                j += 1

            maxEvenLen = 0
            j = 0
            while 0 <= i-j <= i+j+1 <= n-1 and s[i-j] == s[i+j+1]:
                maxEvenLen = (2*j+2)
                if maxEvenLen > res:
                    string = s[i-j:i+j+2]
                    res = maxEvenLen
                j += 1

            i += 1

        return string