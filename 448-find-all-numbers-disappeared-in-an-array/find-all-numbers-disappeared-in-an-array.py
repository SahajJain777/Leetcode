class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        freq = {}
        result = []

        for num in nums:
            freq[num] = freq.get(num,0) + 1 

        for i in range(1,len(nums)+1):
            if i not in freq:
                result.append(i)
        
        return result


        