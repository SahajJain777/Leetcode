class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        finalcount = 0
        for i in nums:
            count = 0

            while (i>0):
                count += 1
                i = i//10   
                print(i)
            if (count%2==0): 
                finalcount += 1
                print(i)

        return finalcount