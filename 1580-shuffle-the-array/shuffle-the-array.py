class Solution(object):
    def shuffle(self, nums, n):
        x = 0
        y = n

        l = []
        for i in range(n):
            l.append(nums[x])
            l.append(nums[y])
            x += 1
            y += 1
        

        return l 
        