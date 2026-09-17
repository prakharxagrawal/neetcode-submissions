class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        first_word = strs[0]
        for i, char in enumerate(first_word):
            for other_word in strs[1:]:
                if i >= len(other_word) or other_word[i] != char:
                    return first_word[:i]

        return first_word