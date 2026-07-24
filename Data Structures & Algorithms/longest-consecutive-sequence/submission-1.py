class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # use a set for constant time look ups
        # use current max and global max
        # as we increment the current max, we pop the element out of the se
        # this ensures we stay O(n)
        # only start counting when n-1 does not exist in unique nums

        unique_nums = set(nums)
        global_max = 0

        for num in unique_nums:
            current_max = 1
            if num - 1 not in unique_nums:
                while (num + current_max) in unique_nums:
                    current_max += 1
                if current_max > global_max:
                    global_max = current_max
        
        return global_max
                

