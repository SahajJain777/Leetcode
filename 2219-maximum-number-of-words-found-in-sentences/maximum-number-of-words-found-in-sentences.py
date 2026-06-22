class Solution(object):
    def mostWordsFound(self, sentences):
        maxcount = 0
        for sentence in sentences:
            count = 0
            for char in sentence:
                if char == " ":
                    count += 1
            if count>maxcount: maxcount = count
        

        return maxcount+1
