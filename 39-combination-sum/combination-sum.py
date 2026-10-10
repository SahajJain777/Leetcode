class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        curr = []

        def backtrack(i, rt):
            # Base case: target reached
            if rt == 0:
                result.append(curr.copy())
                return

            # Stop if target exceeded or candidates exhausted
            if rt < 0 or i >= len(candidates):
                return

            # Choice 1: Take the current number
            curr.append(candidates[i])
            backtrack(i, rt - candidates[i])
            curr.pop()

            # Choice 2: Skip the current number
            backtrack(i + 1, rt)

        backtrack(0, target)
        return result