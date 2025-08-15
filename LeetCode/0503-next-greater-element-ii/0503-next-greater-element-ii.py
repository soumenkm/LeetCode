class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = [nums[-1]]
        n = len(nums)
        for i in range(n-2, -1, -1):
            top = stack[-1]
            elem = nums[i]
            while elem > top:
                stack.pop()
                if len(stack) == 0:
                    break
                else:
                    top = stack[-1]
            stack.append(elem)
        
        res = [-1 for i in range(n)]
        for i in range(n-1, -1, -1):
            top = stack[-1]
            elem = nums[i]
            while elem >= top:
                stack.pop()
                if len(stack) == 0:
                    top = -1
                    break
                else:
                    top = stack[-1]
            res[i] = top
            stack.append(elem)
        
        return res