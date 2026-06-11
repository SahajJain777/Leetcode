class Solution(object):
    def majorityElement(self, nums):

        freq = {}
        n = len(nums)

        for num in nums:
            freq[num] = freq.get(num,0)+1
        
        for key,value in freq.items():
            if value > (n/2):
                return key
        