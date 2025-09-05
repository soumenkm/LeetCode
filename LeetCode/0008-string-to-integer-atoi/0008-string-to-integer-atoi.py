class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        n = len(s)
        i = 0
        res = 0
        
        while i < n and s[i] == " ":
            i += 1
        
        if i < n and s[i] == "+":
            sign = 1
            i += 1
        elif i < n and s[i] == "-":
            sign = -1
            i += 1
        
        while i < n and s[i] == "0":
            i += 1
        
        while i < n and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1

        res = res * sign
        
        if res > 2**31-1:
            res = 2**31-1
        elif res < -2**31:
            res = -2**31
        
        return res

