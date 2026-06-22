class Solution(object):
    def addDigits(self, num):

        #inner loop will just add the number
        #outer loop will check if the nmber is greater than 10 or not
        number = num
        while(num>=10):
            sum = 0
            while(num>0):
                digit = num%10
                num = num/10
                sum = sum + digit
            num = sum
        
        return num
            