import math
class Solution:
    def removeDuplicate(self, arr, last):
        res = [last]
        for elem in arr:
            if res[-1] != elem:
                res.append(elem)
        return res[1:]
        
    def findUnion(self, a, b):
        # code here 
        m = len(a)
        n = len(b)
        res = [-math.inf]
        
        i = 0
        j = 0
        while i < m and j < n:
            if a[i] <= b[j]:
                if res[-1] != a[i]:
                    res.append(a[i])
                i += 1
            else:
                if res[-1] != b[j]:
                    res.append(b[j])
                j += 1
        
        if i == m:
            remain = self.removeDuplicate(arr=b[j:n], last=res[-1])
        elif j == n:
            remain = self.removeDuplicate(arr=a[i:m], last=res[-1])
        
        res = res[1:] + remain
        return res
        
            