class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = [nums2[-1]]
        m = len(nums1)
        n = len(nums2)
        res = {nums2[i]: -1 for i in range(n)}
        for i in range(n-2, -1, -1):
            elem = nums2[i]
            top = stack[-1]
            while elem > top:
                stack.pop()
                if not stack:
                    top = -1
                    break
                top = stack[-1]
            res[elem] = top
            stack.append(elem)
        
        finalRes = []
        for num in nums1:
            finalRes.append(res[num])
        
        return finalRes

