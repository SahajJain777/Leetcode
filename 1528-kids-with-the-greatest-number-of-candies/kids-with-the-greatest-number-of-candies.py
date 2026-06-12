class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):

        maxi = 0
        l = []
        for num in candies:
            if maxi < num: maxi = num
        
        for i in candies:
            if i + extraCandies >=  maxi: l.append(True)
            else : l.append(False)
        
        return l