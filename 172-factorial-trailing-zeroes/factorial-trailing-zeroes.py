class Solution(object):
    def trailingZeroes(self, n):
        
        if (n<=4): return 0
        count = 0

        while(n>=5):
            count = count+(n/5)
            n = n/5

        return count
        