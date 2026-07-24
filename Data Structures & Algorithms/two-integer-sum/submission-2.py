class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for k, v in enumerate(nums):
            complement = target - v
            if complement in seen:
                return [seen[complement], k]
            else:
                seen[v] = k
                