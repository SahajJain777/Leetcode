class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        for i in range(len(nums)):

            left = float('-inf')
            right = float('-inf')

            if i > 0:
                left = nums[i - 1]

            if i < len(nums) - 1:
                right = nums[i + 1]

            if nums[i] > left and nums[i] > right:
                return i