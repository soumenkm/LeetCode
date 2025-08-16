class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        stack = [(arr[-1], n-1)]
        nse = [(-1, n) for i in range(n)]
        for i in range(n-2, -1, -1):
            elem = (arr[i], i)
            top = stack[-1]
            while elem[0] < top[0]:
                stack.pop()
                if not stack:
                    top = (-1, n)
                    break
                else:
                    top = stack[-1]
            nse[i] = top
            stack.append(elem)
        
        stack = [(arr[0], 0)]
        pse = [(-1, -1) for i in range(n)]
        for i in range(1, n, 1):
            elem = (arr[i], i)
            top = stack[-1]
            while elem[0] <= top[0]:
                stack.pop()
                if not stack:
                    top = (-1, -1)
                    break
                else:
                    top = stack[-1]
            pse[i] = top
            stack.append(elem)
        
        cont = 0
        for i in range(n):
            numLeftSubArr = i - pse[i][1]
            numRightSubArr = nse[i][1] - i
            cont = (cont + (numLeftSubArr * numRightSubArr * arr[i]) % MOD) % MOD
        
        return cont
