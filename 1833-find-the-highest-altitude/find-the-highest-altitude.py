class Solution(object):
    def largestAltitude(self, gain):
        
        maxi = 0
        current_height = 0
        for num in gain:
            current_height = current_height + num
            if current_height > maxi : maxi = current_height
        
        return maxi