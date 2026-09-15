class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Base check: strings of different lengths cannot be anagrams
        if len(s) != len(t):
            return False

        char_count = {}

        # Step 1: Count character frequencies in s
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # Step 2: Decrement counts using characters in t
        for char in t:
            # If char was never in s, or we have already matched all occurrences
            if char not in char_count or char_count[char] == 0:
                return False
            char_count[char] -= 1

        return True