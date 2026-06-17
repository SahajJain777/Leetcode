# class Solution:
#     def groupAnagrams(self, strs):
#         groups = {}

#         for word in strs:
#             key = "".join(sorted(word))

#             if key not in groups:
#                 groups[key] = []

#             groups[key].append(word)

#         return list(groups.values())


class Solution:
    def groupAnagrams(self, strs):
        groups = {}

        for word in strs:
            # Count frequencies of 'a' to 'z'
            count = [0] * 26

            for char in word:
                index = ord(char) - ord('a')
                count[index] += 1

            # Lists can't be dictionary keys, so convert to tuple
            key = tuple(count)

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())
