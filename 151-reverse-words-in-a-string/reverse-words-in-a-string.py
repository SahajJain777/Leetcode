class Solution:
    def reverseWords(self, s: str) -> str:
        
        result = []
        arr = s.split()
        arr.reverse()
        result = " ".join(arr)

        return result

