class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        #[1,2,3,4] = 1 + 3 = 4
        #[1,2,2,5,6,6] = 1 + 2 + 6 = 10
        sumi = 0
        nums.sort()

        for i in range(0,len(nums),+2):
            sumi += nums[i]
        
        return sumi
