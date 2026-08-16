class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # current max, global max
        # since the algorithm must be O(n) we cant sort
        # cant assume sorted, have to do set lookup
        numSet = set(nums)
        globalMax = 0
        
        for num in numSet:
            currMax = 1
            if num - 1 not in numSet:
                while (num + currMax) in numSet:
                    currMax += 1
                globalMax = max(globalMax, currMax)
        
        return globalMax

