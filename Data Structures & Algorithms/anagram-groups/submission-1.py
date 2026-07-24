from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        answer = []
        for word in strs: 
            sorted_word = ''.join(sorted(word))
            ans[sorted_word].append(word)
        
        answer = [value for value in ans.values()]
        return answer
            