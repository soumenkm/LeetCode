class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        B = 31
        MOD = 10**9 + 7

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
        
        k = math.ceil(len(b) / len(a))
        string = a * k 
        if subStrMatch(string, b):
            return k
        elif subStrMatch(string+a, b):
            return k+1
        else:
            return -1
        