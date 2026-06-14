class Solution(object):
    def sumOfUnique(self, nums):

        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        
        sum = 0
        for key, value in freq.items():
            if value == 1:
                sum = sum + key
        
        return sum