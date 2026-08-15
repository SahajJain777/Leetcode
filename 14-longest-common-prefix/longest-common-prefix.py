from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        bench = strs[0]
        result = ""

        for i in range(len(bench)):
            for j in range(len(strs)):

                if i >= len(strs[j]):
                    return result

                if strs[j][i] != bench[i]:
                    return result

            result = result + bench[i]

        return result