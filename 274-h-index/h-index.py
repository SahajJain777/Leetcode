class Solution(object):
    def hIndex(self, citations):
        citations.sort()

        max_cur = 0
        n = len(citations)

        for i in range(n):
            current = min(citations[i], n - i)
            max_cur = max(max_cur, current)

        return max_cur