class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cand1 = None
        cand2 = None
        vote1 = 0
        vote2 = 0
        for num in nums:
            if vote1 == 0 and cand2 != num:
                cand1 = num
            elif vote2 == 0 and cand1 != num:
                cand2 = num
            if cand1 == num:
                vote1 += 1
            elif cand2 == num:
                vote2 += 1
            else:
                vote1 -= 1
                vote2 -= 1

        count1 = 0
        count2 = 0
        for num in nums:
            if cand1 == num:
                count1 += 1
            if cand2 == num:
                count2 += 1
        
        res = []
        if count1 > n // 3:
            res.append(cand1)
        if count2 > n // 3:
            res.append(cand2)
        return res