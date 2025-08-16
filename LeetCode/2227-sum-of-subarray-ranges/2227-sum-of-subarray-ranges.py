class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []
        nse = [None for i in range(n)]
        for i in range(n-1, -1, -1):
            elem = (nums[i], i)
            while stack and elem[0] < stack[-1][0]:
                stack.pop()
            if stack:
                nse[i] = stack[-1]
            else:
                nse[i] = (-1, n)
            stack.append(elem)
        
        stack = []
        nge = [None for i in range(n)]
        for i in range(n-1, -1, -1):
            elem = (nums[i], i)
            while stack and elem[0] > stack[-1][0]:
                stack.pop()
            if stack:
                nge[i] = stack[-1]
            else:
                nge[i] = (-1, n)
            stack.append(elem)

        stack = []
        pse = [None for i in range(n)]
        for i in range(n):
            elem = (nums[i], i)
            while stack and elem[0] <= stack[-1][0]:
                stack.pop()
            if stack:
                pse[i] = stack[-1]
            else:
                pse[i] = (-1, -1)
            stack.append(elem)

        stack = []
        pge = [None for i in range(n)]
        for i in range(n):
            elem = (nums[i], i)
            while stack and elem[0] >= stack[-1][0]:
                stack.pop()
            if stack:
                pge[i] = stack[-1]
            else:
                pge[i] = (-1, -1)
            stack.append(elem)

        cont = 0
        for i in range(n):
            mini = (nse[i][1] - i) * (i - pse[i][1]) * nums[i]
            maxi = (nge[i][1] - i) * (i - pge[i][1]) * nums[i]
            cont += maxi - mini
        
        return cont
            