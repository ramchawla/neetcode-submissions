class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_s = {}
        seen_t = {}
        if len(s) != len(t):
            return False
        for letter in s:
            if letter not in seen_s:
                seen_s[letter] = 1
            seen_s[letter] += 1
            
        
        for letter in t:
            if letter not in seen_t:
                seen_t[letter] = 1
            seen_t[letter] += 1

        return seen_s == seen_t