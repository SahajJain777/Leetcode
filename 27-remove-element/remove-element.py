class Solution(object):
    def removeElement(self, nums, val):

        index = 0

        for num in range(len(nums)):
            if(nums[num]!=val):
                nums[index] = nums[num]
                index = index + 1
        
        return index
        

