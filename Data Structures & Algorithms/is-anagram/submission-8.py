class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = {}
        count2 = {}
        for letter in s:
            if letter in count1:
                count1[letter] += 1
            else: 
                count1[letter] = 1
        
        for letter in t:
            if letter in count2:
                count2[letter] += 1
            else: count2[letter] = 1
        
        return count1 == count2