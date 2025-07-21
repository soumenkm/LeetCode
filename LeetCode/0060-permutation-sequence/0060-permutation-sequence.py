class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1, n+1)]

        def func(nums: List[int], k: int) -> str:
            n = len(nums)
            if n == 1:
                return str(nums[0])
            else:
                q, r = divmod(k, math.factorial(n-1))
                elem = nums[q]
                nums.remove(elem)
                res = func(nums, r)
                return str(elem) + res
        
        res = func(nums, k-1)
        return res