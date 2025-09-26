class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = 0
        j = n - 1

        count = 0
        while j >= 0 and i <= n-1 and i <= j:
            if nums[j] == val:
                j -= 1
                count += 1
                continue
            if nums[i] != val:
                i += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
                count += 1

        print(count)
        return n - count
