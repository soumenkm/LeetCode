class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        penalty = 0
        for char in s:
            if char == "(":
                count += 1
            elif char == ")":
                if count > 0:
                    count -= 1
                elif count == 0:
                    penalty += 1
        
        return count + penalty
                
                
        
        