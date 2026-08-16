class Solution(object):
    def fib(self, n):
        
        if n==0: return 0
        if n==1: return 1
        x = 0
        y = 1

        for i in range(2,n+1):
            c = x + y
            x = y
            y = c
        
        return y
