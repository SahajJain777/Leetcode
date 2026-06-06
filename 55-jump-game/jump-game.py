class Solution(object):
    def canJump(self, nums):
        i = 0
        n = len(nums)

        while i < n:
            if i >= n - 1:
                return True

            best_i = i
            best_reach = i

            for j in range(i + 1, min(n, i + nums[i] + 1)):
                if j + nums[j] > best_reach:
                    best_reach = j + nums[j]
                    best_i = j

            if best_i == i:
                return False

            i = best_i

        return False