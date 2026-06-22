class Solution(object):
    def firstPalindrome(self, words):

        for word in words:
            left = 0
            right = len(word) - 1
            flag = 0

            while left < right:
                if word[left] == word[right]:
                    left += 1
                    right -= 1
                else:
                    flag = 1
                    break

            if flag == 0:
                return word

        return ""