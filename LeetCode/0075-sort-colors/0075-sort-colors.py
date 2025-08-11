class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        hashMap = {0: 0, 1:0, 2:0}
        for i in range(n):
            hashMap[nums[i]] += 1
        
        # print(hashMap)
        for i in range(n):
            if 0 <= i < hashMap[0]:
                nums[i] = 0
            elif hashMap[0] <= i < hashMap[1] + hashMap[0]:
                nums[i] = 1
            else:
                nums[i] = 2