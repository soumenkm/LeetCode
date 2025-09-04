class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
            
        signNum = 1 if dividend >= 0 else -1
        signDen = 1 if divisor >= 0 else -1
        num = abs(dividend)
        den = abs(divisor)

        def div(num: int, den: int) -> int:
            ans = 0
            while num >= den:
                i = 0
                while (den << i) <= num:
                    i += 1
                ans += (1 << (i-1))
                num -= den << (i-1)
            return ans
        
        if signNum * signDen == 1:
            return div(num, den)
        else:
            return -div(num, den)