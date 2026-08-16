class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        freq = {}

        # Count elements in arr1
        for num in arr1:
            freq[num] = freq.get(num, 0) + 1

        result = []

        # Put arr2 elements first
        for num in arr2:
            result += [num] * freq[num]
            del freq[num]

        # Remaining elements in ascending order
        remaining = []

        for num in freq:
            remaining += [num] * freq[num]

        remaining.sort()

        result += remaining

        return result