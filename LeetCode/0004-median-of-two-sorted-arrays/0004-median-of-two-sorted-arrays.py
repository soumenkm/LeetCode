class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
         
        def BS(low: int, high: int) -> int:
            nonlocal n1
            nonlocal n2

            mid = (low + high) // 2
            numsLeft = (n1 + n2 + 1) // 2
            k = numsLeft - mid
            l1 = nums1[mid-1] if mid > 0 else -math.inf
            l2 = nums2[k-1] if k > 0 else -math.inf
            r1 = nums1[mid] if mid < n1 else math.inf
            r2 = nums2[k] if k < n2 else math.inf
            
            if (l2 <= r1) and (l1 <= r2):
                if (n1 + n2) % 2 == 1:
                    med = max(l1, l2)
                else:
                    med = (max(l1, l2) + min(r1, r2)) / 2
                return med
            elif l2 > r1:
                return BS(mid+1, high)
            elif l1 > r2:
                return BS(low, mid-1)

        return BS(0, n1)
