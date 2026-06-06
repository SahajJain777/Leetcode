class Solution(object):
    def maximumProduct(self, nums):

        nums.sort()
        highest = nums[-1] * nums [-2] * nums[-3]
        negative = nums[0] * nums[1] * nums[-1]

        ans = max(highest,negative)
        return ans
        