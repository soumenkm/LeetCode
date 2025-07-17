class Solution:
    def myPow(self, x: int, n: int) -> int:
        MOD = 10**9 + 7
        # Base case for the recursion
        if n == 0:
            return 1
        
        # 1. Recursively compute x^(n/2)
        half = self.myPow(x, n // 2)
        
        # 2. Square the result to get x^n for even n
        res = (half * half) % MOD
        
        # 3. If n is odd, we need one more multiplication by x
        if n % 2 == 1:
            res = (res * x) % MOD
            
        return res

    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Number of even-indexed positions (0, 2, 4...)
        # This is ceil(n/2)
        even_positions = (n + 1) // 2
        
        # Number of odd-indexed positions (1, 3, 5...)
        # This is floor(n/2)
        odd_positions = n // 2
        
        res1 = self.myPow(5, even_positions)
        res2 = self.myPow(4, odd_positions)
        
        return (res1 * res2) % MOD