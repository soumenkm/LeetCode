class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap = defaultdict(int)
        maxFreq = 0
        maxLen = 0
        n = len(s)
        left = 0
        right = 0

        while right < n:
            char = s[right]
            currLen = right - left + 1
            hashMap[char] += 1
            maxFreq = max(maxFreq, hashMap[char])

            if currLen - maxFreq <= k:
                maxLen = max(maxLen, currLen)
            else:
                hashMap[s[left]] -= 1
                left += 1
            right += 1
        
        return maxLen