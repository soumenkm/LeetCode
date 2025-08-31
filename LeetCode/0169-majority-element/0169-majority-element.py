class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # hashMap = defaultdict(int)
        # n = len(nums)
        # for num in nums:
        #     hashMap[num] += 1
        #     if hashMap[num] > n // 2:
        #         return num

        # count = 0
        # for num in nums:
        #     if count == 0:
        #         elem = num
        #     if num == elem:
        #         count += 1
        #     else:
        #         count -= 1
        # return elem
        
        cand = None
        vote = 0
        for num in nums:
            if vote == 0:
                cand = num
                vote = 1
            elif num == cand:
                vote += 1
            else:
                vote -= 1
        
        return cand
