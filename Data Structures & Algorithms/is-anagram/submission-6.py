from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_s = defaultdict(int)
        seen_t = defaultdict(int)

        for letter in s:
            seen_s[letter] += 1
        
        for letter in t:
            seen_t[letter] += 1
        
        return seen_s == seen_t

        