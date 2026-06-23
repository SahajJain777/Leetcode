class Solution(object):
    def xorOperation(self, n, start):

        ans = 0
        num = start
        for i in range(n):
            ans = num ^ ans
            num = num + 2

        

        return ans