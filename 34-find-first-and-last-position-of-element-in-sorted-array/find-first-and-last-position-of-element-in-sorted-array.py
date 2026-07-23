class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def firstOccurrence():
            left = 0
            right = len(nums) - 1
            answer = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    answer = mid
                    right = mid - 1      # Keep searching left
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return answer

        def lastOccurrence():
            left = 0
            right = len(nums) - 1
            answer = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    answer = mid
                    left = mid + 1       # Keep searching right
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return answer

        return [firstOccurrence(), lastOccurrence()]