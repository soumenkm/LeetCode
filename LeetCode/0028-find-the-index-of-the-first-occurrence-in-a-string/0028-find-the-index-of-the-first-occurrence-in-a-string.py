class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def KMP(string: str) -> List[int]:
            # Returns the KMP table
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
        
            return LPS
        
        LPS = KMP(needle)
        n = len(haystack)
        m = len(needle)
        i = 0
        j = 0
        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            
            if j == m:
                return i - j
            elif i < n and haystack[i] != needle[j]:
                if j == 0:
                    i += 1
                else:
                    j = LPS[j-1]
                
        return -1
