class Solution:
    def largestOddNumber(self, num: str) -> str:
        i = len(num) - 1
        while i >= 0:
            if int(num[i]) % 2 == 1:
                break
            i -= 1
        return num[0:i+1]
