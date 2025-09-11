#User function Template for python3
class Solution:
	def perfectSum(self, arr, target):
		n = len(arr)
		DP = [[0 for i in range(target+1)] for i in range(n)]
		DP[0][0] = 1
		if arr[0] <= target:
		    DP[0][arr[0]] += 1
		
		for i in range(1, n):
		    for j in range(target+1):
		        resNotTake = DP[i-1][j]
		        newTarget = j - arr[i]
		        resTake = 0
		        if newTarget >= 0:
		            resTake = DP[i-1][newTarget]
		        res = resTake + resNotTake
		        DP[i][j] = res
	    
	    return DP[n-1][target]