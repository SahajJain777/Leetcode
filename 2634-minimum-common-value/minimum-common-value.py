class Solution(object):
    def getCommon(self, nums1, nums2):

        n1 = 0
        n2 = 0
        count = -1
        while(n1<len(nums1) and n2<len(nums2)):
            if nums1[n1] == nums2[n2]:
                return nums1[n1]
            
            else:
                if nums1[n1] < nums2[n2]:
                    n1 +=1
                else:
                    n2 += 1
        
        return -1
