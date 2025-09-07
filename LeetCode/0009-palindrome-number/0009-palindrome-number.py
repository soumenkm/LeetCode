class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        num = 0
        orig = x
        while x > 0:
            x, rem = divmod(x, 10)
            num = num * 10 + rem
    
        return num == orig