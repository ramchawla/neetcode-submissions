class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupe_free = set(nums)
        return len(dupe_free) != len(nums)
        