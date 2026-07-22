class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        maxdif = 0
        #(9,6,3,1)
        for i in range(len(nums)-1):
            dif = nums[i] - nums[i+1]
            if dif>maxdif: maxdif = dif
        
        return maxdif
