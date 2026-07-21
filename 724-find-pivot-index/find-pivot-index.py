class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lsum = []
        rsum = []
        l = 0
        r = 0
        for i in range(len(nums)):
            lsum.append(nums[i] + l)
            l = l + nums[i]
        
        for i in range(len(nums)-1,-1,-1):
            rsum.append(nums[i] + r)
            r = r + nums[i]

        rsum.reverse()

        for i in range(len(nums)):
            if lsum[i] == rsum[i]:
                return i
        
        return -1

