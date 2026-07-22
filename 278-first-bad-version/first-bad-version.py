# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        mid = n
        # 1 2 3 4 5 6 7 8 9 10
        # F F F F F T T T T T 

        while(left<right):
            mid = (left + right) // 2
            if isBadVersion(mid) == True:
                right = mid
                continue
            else:
                left = mid + 1
                continue

        return left