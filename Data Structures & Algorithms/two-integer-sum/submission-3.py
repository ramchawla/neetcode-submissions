class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use a hashmap to keep track of what we've already seen
        # then look for complement in there
        # need to return the indices

        seen = {}

        for index, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], index]
            seen[num] = index
        
        