class Solution(object):
    def singleNonDuplicate(self, nums):

        if(len(nums)==1):
            return nums[0]
        
        count = 0
        for i in range(1,len(nums),+2):
            count += 2

            if(nums[i]!=nums[i-1]): #it checks every 2 element 
                return nums[i-1]
            
            if(count==len(nums)-1):
                return nums[len(nums)-1]
        