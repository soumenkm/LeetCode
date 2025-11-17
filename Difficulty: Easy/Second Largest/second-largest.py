class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        firstMax = arr[0]
        secMax = 0
        n = len(arr)
        for i in range(1, n):
            elem = arr[i]
            if elem > firstMax:
                secMax = firstMax
                firstMax = elem
            elif elem == firstMax:
                continue
            elif elem > secMax:
                secMax = elem
        
        if firstMax == secMax:
            return -1
        else:
            return secMax