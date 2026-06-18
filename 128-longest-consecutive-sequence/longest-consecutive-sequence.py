class Solution(object):
    def longestConsecutive(self, nums):
        nums.sort()
        #first sort the array
        #In each iteration check ir the next number is one larger than the current number
        #keep the maximum count you have got
        #run this till the second last element 

        maxcount = 0
        current_count = 0

        if len(nums) == 0: return 0
        for i in range(len(nums)-1):
            if nums[i]+1 == nums[i+1]:
                current_count += 1
                if maxcount<current_count: maxcount = current_count
            elif nums[i] == nums[i+1]:
                continue
            else:
                current_count = 0
        
        return maxcount+1
