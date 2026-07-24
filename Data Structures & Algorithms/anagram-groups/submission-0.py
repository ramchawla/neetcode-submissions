from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = defaultdict(list)
        for s in strs:
            sorted_word = "".join(sorted(s))
            sorted_strs[sorted_word] += [s]
        return list(sorted_strs.values())