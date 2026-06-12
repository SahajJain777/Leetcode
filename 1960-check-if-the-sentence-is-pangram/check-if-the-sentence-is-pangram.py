class Solution(object):
    def checkIfPangram(self, sentence):

        s = set()

        flag = True
        for s1 in sentence:
            s.add(s1)
        
        return (len(s) == 26)