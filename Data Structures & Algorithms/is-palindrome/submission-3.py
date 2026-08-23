class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 2 pointer approach
        # remove spaces and non-ascii chars
        # check if right pointer == left pointer and then shrink

        clean_s = s.lower()
        l, r = 0, len(clean_s) - 1

        while l < r:
            while l < r and not clean_s[l].isalnum():
                l += 1
            while l < r and not clean_s[r].isalnum():
                r -= 1
            if clean_s[l] == clean_s[r]:
                l += 1
                r -= 1
            else:
                return False
        
        return True
        
            
