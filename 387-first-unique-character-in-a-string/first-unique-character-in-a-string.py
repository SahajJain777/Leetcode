class Solution(object):
    def firstUniqChar(self, s):
        #we have to find the index at with the unique letter exits
        #first we will find the frequency of all the elements
        #Then we will check whose frequency is equal to 1
        #then we will iterate again in the s, and if that particular char is equal to the element with freqency 1, we will return it 

        freq = {}
        flag = 0
        unique = ""
        for char in s:
            freq[char] = freq.get(char,0) + 1
        
        
        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i

        return -1