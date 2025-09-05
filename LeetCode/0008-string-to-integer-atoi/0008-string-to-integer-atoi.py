class Solution:
    def myAtoi(self, s: str) -> int:
        nums = []
        sign = 1
        n = len(s)
        i = 0
        
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
            nums.append(s[i])
            i += 1

        m = len(nums)
        res = 0
        for i in range(m):
            res = res * 10 + int(nums[i])
        res = res * sign

        if res > 2**31-1:
            res = 2**31-1
        elif res < -2**31:
            res = -2**31
        
        return res

