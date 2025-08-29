class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        if n < 4:
            return []

        res = []
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                modTarget = target - nums[i] - nums[j]
                k = j + 1
                l = n - 1
                while k < l:
                    sumVal = nums[k] + nums[l]
                    if sumVal == modTarget:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        while k < l and nums[k-1] == nums[k]:
                            k += 1
                        l -= 1
                        while k < l and nums[l] == nums[l+1]:
                            l -= 1
                    elif sumVal < modTarget:
                        k += 1
                    elif sumVal > modTarget:
                        l -= 1
        
        return res