# class Solution:
#     def getPermutation(self, n: int, k: int) -> str:
#         nums = [i for i in range(1, n+1)]

#         def func(nums: List[int], k: int) -> str:
#             n = len(nums)
#             if n == 1:
#                 return str(nums[0])
#             else:
#                 q, r = divmod(k, math.factorial(n-1))
#                 elem = nums[q]
#                 nums.remove(elem)
#                 res = func(nums, r)
#                 return str(elem) + res
        
#         res = func(nums, k-1)
#         return res

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = list(range(1, n + 1))
        # No need to pre-calculate all factorials.
        
        result = []
        k -= 1 # Use 0-indexed k
        
        for i in range(n, 0, -1):
            # Calculate the factorial for the block size on the fly
            block_size = math.factorial(i - 1)
            
            # index = k // block_size
            # k = k % block_size
            index, k = divmod(k, block_size) # A more Pythonic way to do it
            
            digit = numbers[index]
            result.append(str(digit))
            
            # The O(n) operation
            numbers.pop(index)
            
        return "".join(result)