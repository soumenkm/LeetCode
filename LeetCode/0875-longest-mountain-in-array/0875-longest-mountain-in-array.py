class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        def getDP(arr: List[int]) -> List[int]:
            n = len(arr)
            DP = [1 for i in range(n)]
            for i in range(1, n):
                for j in range(i-1, i):
                    if arr[j] < arr[i]:
                        DP[i] = max(DP[i], 1 + DP[j])
            return DP
        
        n = len(arr)
        if n < 3:
            return 0
        
        # 1. Get the uphill lengths (left to right)
        DPF = getDP(arr)
        
        # 2. Get the "downhill" lengths (right to left)
        # We do this by reversing the array, running getDP, and then we MUST reverse the result.
        arr_rev = arr[::-1]
        DPR_rev = getDP(arr_rev)
        DPR = DPR_rev[::-1] # Reverse the result to align with original indices
        
        # 3. Combine the results correctly
        max_length = 0
        for i in range(n):
            # A valid mountain peak must have both an uphill and a downhill part.
            # A length of 1 means it's just the peak itself with no slope.
            if DPF[i] > 1 and DPR[i] > 1:
                current_length = DPF[i] + DPR[i] - 1
                max_length = max(max_length, current_length)
                
        return max_length
