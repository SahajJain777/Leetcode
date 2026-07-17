class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        result = []
        currentsum = 0
        count = 0
        for num in nums:
            currentsum = num + currentsum
            result.append(currentsum)
            count += 1
        
        return result
