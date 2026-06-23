class Solution(object):
    def numberGame(self, nums):
        #this is clearly a stack question in which we will pop minimum elements for the array
        # and add it in the stack first bob then alice

        numsort = sorted(nums)
        ans = []
        for i in range(1,len(nums),2):
            ans.append(numsort[i])
            ans.append(numsort[i-1])
        
        return ans
            

        