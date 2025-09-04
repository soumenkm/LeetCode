class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        B = 31
        MOD = 10**9 + 1
        if len(s) != len(goal):
            return False

        def getHash(string: str) -> int:
            nonlocal B
            nonlocal MOD
            hashVal = 0
            for char in string:
                hashVal = (hashVal * B + ord(char)) % MOD
            return hashVal
        
        def isSame(s1: str, s2: str) -> bool:
            n = len(s1)
            for i in range(n):
                if s1[i] != s2[i]:
                    return False
            return True

        def subStrMatch(s: str, t: str) -> bool:
            nonlocal B
            nonlocal MOD
            n = len(s)
            m = len(t)
            numWindows = n - m + 1
            hashT = getHash(t)
            P = B ** (m-1)

            hashWindow = getHash(s[0:0+m])
            for i in range(numWindows):
                if hashWindow == hashT:
                    if isSame(s[i:i+m], t):
                        return True
                if i < numWindows-1:
                    hashWindow = (((((hashWindow - ord(s[i]) * P) % MOD) + MOD) % MOD) * B + ord(s[i+m])) % MOD
            return False
        
        string = s + s
        res = subStrMatch(string, goal)
        return res
