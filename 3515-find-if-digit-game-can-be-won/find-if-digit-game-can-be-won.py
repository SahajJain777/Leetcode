class Solution(object):
    def canAliceWin(self, nums):

        doubledigitsum = 0
        singledigitsum = 0
        for num in nums:
            if num >= 10:
                doubledigitsum += num
            
            else:
                singledigitsum += num
        
        if singledigitsum == doubledigitsum: return False
        else: return True

            
