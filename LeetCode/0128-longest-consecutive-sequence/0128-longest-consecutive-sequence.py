class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        maxLen = 0
        for num in hashSet:
            if num-1 in hashSet:
                continue
            else:
                length = 0
                elem = num
                while elem in hashSet:
                    length += 1
                    elem += 1
                maxLen = max(maxLen, length)
        return maxLen