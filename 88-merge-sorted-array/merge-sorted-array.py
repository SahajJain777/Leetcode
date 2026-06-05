class Solution(object):
    def merge(self, nums1, m, nums2, n):
        
        j = 0
        for num in range(m,len(nums1)):
            nums1[num] = nums2[j]
            j+=1
        
        nums1.sort()

        return nums1