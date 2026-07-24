from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        ans = []

        for num in nums:
            count[num] += 1
        
        sorted_dict = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
        keys = list(sorted_dict)
        ans = keys[:k]
        
        return ans
            
