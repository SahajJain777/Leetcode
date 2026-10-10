class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        subset = []

        def backtrack(i):
        #base case
            if i == len(nums):
                result.append(subset.copy())
                return
        
            #choose condition
            subset.append(nums[i])
            backtrack(i+1)

            subset.pop()
            backtrack(i+1)

        backtrack(0)
        return result


