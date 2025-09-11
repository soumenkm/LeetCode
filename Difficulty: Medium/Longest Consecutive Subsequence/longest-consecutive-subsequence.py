 #User function Template for python3
 
class Solution:
    
    # arr[] : the input array
    
    #Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self,arr):
        hashSet = set(arr)
        maxLen = 0
        for num in hashSet:
            if num-1 in hashSet:
                continue
            else:
                length = 0
                elem = num
                while elem in hashSet:
                    length += 1
                    elem += 1
                maxLen = max(maxLen, length)
        return maxLen