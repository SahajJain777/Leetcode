class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        n1 = []
        
        for i in range(m):
            n1.append(nums1[i])
        

        n1 = n1 + nums2
        nums1.clear()
        nums1.extend(n1)
        nums1.sort()