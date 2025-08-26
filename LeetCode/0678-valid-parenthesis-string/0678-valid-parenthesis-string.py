class Solution:
    def checkValidString(self, s: str) -> bool:
        mini = 0
        maxi = 0
        for char in s:
            if char == "(":
                mini = mini + 1
                maxi = maxi + 1
            elif char == ")":
                mini = max(0, mini - 1)
                maxi = maxi - 1
            else:
                mini = max(0, mini - 1)
                maxi = maxi + 1
            if maxi == -1:
                return False
        
        if mini == 0:
            return True
        else:
            return False