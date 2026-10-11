class Solution:
    def partitionString(self, s: str) -> int:
        result = []
        current = [s[0]]
        seen = {s[0]}

        for i in range(len(s) - 1):
            if s[i + 1] in seen:
                result.append("".join(current))
                current = [s[i + 1]]
                seen = {s[i + 1]}
            else:
                current.append(s[i + 1])
                seen.add(s[i + 1])

        result.append("".join(current))
        return len(result)