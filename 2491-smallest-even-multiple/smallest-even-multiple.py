class Solution(object):
    def smallestEvenMultiple(self, n):

        flag = True
        multiple = 1
        while flag:
            num = n * multiple
            if(num%2==0):
                return n*multiple
                flag = False
            
            multiple += 1
        
            