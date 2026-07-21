class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(ch.lower() for ch in s if ch.isalnum())
        sr = s[::-1]
        if s == sr:
            return True
        else:
            return False