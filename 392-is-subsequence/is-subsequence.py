class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        sub = 0

        if len(s) == 0 : return True


        for i in range(len(t)):
            
            if(s[sub]==t[i]):
                sub += 1
            
            if(sub == len(s)): return True
        
        if(sub == len(s)): return True
        else : return False