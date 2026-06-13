class Solution(object):
    def numIdenticalPairs(self, nums):
        

        freq = {}
        count = 0

        for i in nums:
            if i in freq:
                count = count + freq[i]
            freq[i] = freq.get(i,0) + 1


        return count



