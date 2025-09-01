class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        hashMap = defaultdict(int)
        left = 0
        right = 0
        maxLen = 0
        
        while right < n:
            char = s[right]
            if char in hashMap and left <= hashMap[char] <= right:
                left = hashMap[char] + 1
            
            hashMap[char] = right
            maxLen = max(maxLen, right-left+1)
            right += 1
        
        return maxLen

