class Solution(object):
    def differenceOfSum(self, nums):
        elementsum = 0
        digitsum = 0
        for num in nums:
            elementsum = elementsum + num
            digit = 0
            while(num>0):
                digit = num%10
                num = num/10
                digitsum = digitsum + digit
            
        
        return abs(elementsum - digitsum)
