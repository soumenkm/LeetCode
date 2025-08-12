class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = 0
        neg = 1
        res = [-1 for i in range(len(nums))]
        for num in nums:
            if num > 0:
                res[pos] = num
                pos = pos + 2
            else:
                res[neg] = num
                neg = neg + 2
        
        return res