class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        pattern_to_word = {}
        word_to_pattern = {}

        for i in range(len(pattern)):
            ch = pattern[i]
            word = words[i]

            if ch in pattern_to_word:
                if pattern_to_word[ch] != word:
                    return False
            else:
                pattern_to_word[ch] = word

            if word in word_to_pattern:
                if word_to_pattern[word] != ch:
                    return False
            else:
                word_to_pattern[word] = ch

        return True