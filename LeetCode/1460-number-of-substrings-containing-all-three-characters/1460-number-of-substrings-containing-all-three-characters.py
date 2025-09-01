class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        a = -1
        b = -1
        c = -1
        n = len(s)
        count = 0

        for i in range(n):
            char = s[i]
            if char == "a":
                a = i
            elif char == "b":
                b = i
            elif char == "c":
                c = i
            
            minIndex = min(a, b, c)
            if minIndex != -1:
                count += minIndex + 1
        
        return count


