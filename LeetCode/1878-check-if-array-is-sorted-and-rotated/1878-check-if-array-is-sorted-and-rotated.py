class Solution:
    def check(self, nums: List[int]) -> bool:
        def isNonDec(i: int, j: int) -> bool:
            while i < j:
                if nums[i+1] < nums[i]:
                    return False
                i = i + 1
            return True
        
        n = len(nums)
        for k in range(0, n):
            res1 = isNonDec(0, n-1-k)
            mini = min(nums[:n-k])
            res2 = None if k == 0 else isNonDec(n-k, n-1)
            maxi = None if k == 0 else max(nums[n-k:])
            if k == 0 and res1:
                return True
            if k > 0 and res1 and res2 and mini >= maxi:
                return True
        
        return False