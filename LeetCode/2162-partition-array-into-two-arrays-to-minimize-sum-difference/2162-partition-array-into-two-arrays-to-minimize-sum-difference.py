# class Solution:
#     def minimumDifference(self, nums: List[int]) -> int:
#         n = len(nums)
#         negSum = sum([i for i in nums if i < 0])
#         posSum = sum([i for i in nums if i >= 0])
#         totalSum = sum(nums)

#         length = n//2
#         prevDP = {i: [False for k in range(length+1)] for i in range(negSum, posSum+1, 1)}
#         prevDP[0][0] = True
#         prevDP[nums[0]][1] = True
                
#         for i in range(1, n):
#             currDP = {i: [False for k in range(length+1)] for i in range(negSum, posSum+1, 1)}
#             for j in range(negSum, posSum+1, 1):
#                 for k in range(length+1):
#                     res1 = prevDP[j][k]
#                     res2 = False
#                     if j-nums[i] >= negSum and j-nums[i] <= posSum and k > 0: 
#                         res2 = prevDP[j-nums[i]][k-1]
#                     res = res1 or res2
#                     currDP[j][k] = res
#             prevDP = currDP
        
#         finalDP = {}
#         for target, lengths in currDP.items():
#             if lengths[n//2]:
#                 finalDP.update({target: abs(totalSum-2*target)})
        
#         return min(finalDP.values())

from typing import List
import bisect

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        half_n = n // 2
        total_sum = sum(nums)

        # Helper function to generate all possible sums for all lengths
        def get_all_sums(arr: List[int]) -> List[List[int]]:
            # sums[k] will store all possible sums using k elements
            sums = [set() for _ in range(half_n + 1)]
            sums[0].add(0) # Base case: sum of 0 with 0 elements

            for num in arr:
                # Iterate backwards to avoid using the same element multiple times in one subset combination
                for k in range(half_n, 0, -1):
                    for s in sums[k - 1]:
                        sums[k].add(s + num)
            
            return [sorted(list(s)) for s in sums]

        # 1. Split the array and get sums for both halves
        left_sums = get_all_sums(nums[:half_n])
        right_sums = get_all_sums(nums[half_n:])

        min_diff = float('inf')

        # 2. Meet in the middle
        # For each possible length 'k' from the left part
        for k in range(half_n + 1):
            # We need to pick 'half_n - k' elements from the right part
            right_k = half_n - k
            
            # For each sum 's1' from the left part
            for s1 in left_sums[k]:
                # We need a sum 's2' from the right part's list
                # such that s1 + s2 is as close to total_sum / 2 as possible.
                # This means s2 should be close to (total_sum / 2) - s1
                
                target_s2 = total_sum / 2 - s1
                
                # Binary search to find the closest s2 in the sorted right_sums list
                r_sums = right_sums[right_k]
                
                # Find insertion point for target_s2
                idx = bisect.bisect_left(r_sums, target_s2)
                
                # Check the candidate at the insertion point
                if idx < len(r_sums):
                    s2 = r_sums[idx]
                    current_sum = s1 + s2
                    min_diff = min(min_diff, abs(total_sum - 2 * current_sum))
                
                # Check the candidate just before the insertion point
                if idx > 0:
                    s2 = r_sums[idx - 1]
                    current_sum = s1 + s2
                    min_diff = min(min_diff, abs(total_sum - 2 * current_sum))

        return int(min_diff)