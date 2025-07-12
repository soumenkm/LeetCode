class Solution:
    @staticmethod
    def twoSumSorted(nums: List[int], target: int) -> List[List[int]]:
        left = 0
        right = len(nums) - 1
        results = set()
        while left < right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            elif left > 0 and nums[left] == nums[left-1]:
                left += 1
            else:
                results.add(tuple(sorted([nums[left], nums[right]])))
                left += 1
        return [list(i) for i in results]
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        results = set()
        for i in range(len(nums)-2):
            a = nums[i]
            if a > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -a
            sliced_nums = nums[i+1:]
            res = Solution.twoSumSorted(sliced_nums, target)
            if len(res) != 0:
                for b, c in res:
                    results.add(tuple(sorted([a, b, c])))
        return [list(i) for i in results]

        