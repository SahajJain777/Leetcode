class Solution(object):
    def countDigits(self, num):

        count = 0
        temp = num
        while num > 0:
            current = num % 10 
            num = num/10

            if(temp%current == 0):
                count += 1
        
        return count