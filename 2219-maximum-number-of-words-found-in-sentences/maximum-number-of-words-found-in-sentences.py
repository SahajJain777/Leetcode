class Solution(object):
    def mostWordsFound(self, sentences):
        max_count = 0

        for sentence in sentences:
            max_count = max(max_count, len(sentence.split()))

        return max_count