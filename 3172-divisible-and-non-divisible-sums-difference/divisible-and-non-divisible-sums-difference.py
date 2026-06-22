class Solution(object):
    def differenceOfSums(self, n, m):
        divi = 0
        nondivi = 0

        for i in range(1,n+1):
            if (i%m == 0):
                divi = divi + i
            else:
                nondivi = nondivi + i
            
        return nondivi - divi