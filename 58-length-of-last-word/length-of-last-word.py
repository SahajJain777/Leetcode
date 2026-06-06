class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c = " "
        i = len(s)
        count = 0
        s = s.strip()

        for i in range(len(s)-1, -1,-1):
            if(s[i] == c):
                break
            count += 1
        
        return count
        