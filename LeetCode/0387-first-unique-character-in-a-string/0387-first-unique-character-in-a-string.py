class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashMap = {}
        for i, char in enumerate(s):
            if char not in hashMap:
                hashMap[char] = [1, i]
            else:
                hashMap[char][0] += 1
        
        for k, v in hashMap.items():
            if v[0] == 1:
                return v[1]

        return -1 
        