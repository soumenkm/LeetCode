class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hashMap = defaultdict(int)
        for char in t:
            hashMap[char] += 1
        
        left = 0
        right = 0
        n = len(s)
        minLen = math.inf
        count = 0
        startIndex = -1
        k = len(t)

        while right < n:
            char = s[right]
            if hashMap[char] > 0:
                count += 1
            hashMap[char] -= 1

            while count >= k:
                currLen = right - left + 1
                if currLen < minLen:
                    minLen = currLen
                    startIndex = left
                hashMap[s[left]] += 1
                if hashMap[s[left]] > 0:
                    count -= 1
                left += 1

            right += 1
        
        if startIndex == -1:
            return ""
        
        return s[startIndex: startIndex + minLen]

