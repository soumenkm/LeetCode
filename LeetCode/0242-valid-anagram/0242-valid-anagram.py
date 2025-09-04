class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashArr = [0 for i in range(26)]
        n = len(s)
        for i in range(n):
            hashArr[ord(s[i]) - ord("a")] += 1
            hashArr[ord(t[i]) - ord("a")] -= 1
        for count in hashArr:
            if count != 0:
                return False
        return True