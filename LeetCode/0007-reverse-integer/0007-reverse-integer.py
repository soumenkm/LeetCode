class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            sign = 1
        else:
            sign = -1
        x = abs(x)
        num = 0
        while x > 0:
            x, rem = divmod(x, 10)
            num = num * 10 + rem
        
        num = num * sign
        if num < -2**31:
            return 0
        elif num > 2**31-1:
            return 0
        else:
            return num
