class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        
        ans = []
        current = intervals[0]

        i = 0
        while(i < len(intervals)-1):

            if current[1] >= intervals[i+1][0]:
                current = [current[0], max(current[1], intervals[i+1][1])]
                i = i + 1

            else:
                ans.append(current)
                current = intervals[i+1]
                i = i + 1

        ans.append(current)

        return ans