class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash = [0 for i in range(26)]
        n = len(s)
        for i in range(n):
            hash[ord(s[i]) - ord("a")] += 1
            hash[ord(t[i]) - ord("a")] -= 1
        for count in hash:
            if count != 0:
                return False
        return True