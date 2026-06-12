class Solution(object):
    def maxDifference(self, s):
        oddmax = 0
        evenmin = 9999
        
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch,0) + 1

        for key,value in freq.items():
            if value%2 == 0:
                if evenmin > value:
                    evenmin = value

            else:
                if oddmax < value:
                    oddmax = value
        
        return oddmax-evenmin