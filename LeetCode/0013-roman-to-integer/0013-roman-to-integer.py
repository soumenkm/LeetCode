class Solution:
    def romanToInt(self, s: str) -> int:
        hashMap = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        n = len(s)
        for i in range(n):
            if i < n-1 and s[i] == "I" and (s[i+1] == "V" or s[i+1] == "X"):
                res -= hashMap[s[i]]
            elif i < n-1 and s[i] == "X" and (s[i+1] == "L" or s[i+1] == "C"):
                res -= hashMap[s[i]] 
            elif i < n-1 and s[i] == "C" and (s[i+1] == "D" or s[i+1] == "M"):
                res -= hashMap[s[i]] 
            else:
                res += hashMap[s[i]]
        
        return res
