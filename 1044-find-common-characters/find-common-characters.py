class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = {}
        result = []

        for letter in words[0]:
            common[letter]  = common.get(letter , 0) + 1



        for i in range(1,len(words)):
            current = {}
            for j in words[i]:
                current[j] = current.get (j,0) + 1

            for key, value in common.items():
                common[key] = min(value, current.get(key, 0))

        for ch, freq in common.items():
            for i in range(freq):
                result.append(ch)

        return result
