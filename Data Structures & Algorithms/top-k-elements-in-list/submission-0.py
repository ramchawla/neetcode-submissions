from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create and populate a dictionary with count for each element
        # sort that dict in reverse with respect to the values
        # pull the sorted dict values into a list
        # splice that list based on the value of k
        res = defaultdict(int)
        for num in nums:
            res[num] += 1
        
        sorted_items_desc = sorted(res.items(), key=lambda item: item[1], reverse=True)

        ans = []
        for item in sorted_items_desc:
            ans.append(item[0])
        
        return ans[:k]