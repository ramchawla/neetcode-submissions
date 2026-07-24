class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # use a set for constant time look ups
        # use current max and global max
        # as we increment the current max, we pop the element out of the se
        # this ensures we stay O(n)
        # only start counting when n-1 does not exist in unique nums

        unique_nums = set(nums)
        seen = set()
        global_max = 0

        if len(nums) == 0:
            return global_max

        for num in unique_nums:
            current_max = 1
            if num in seen:
                continue
            if num - 1 not in unique_nums:
                # unique_nums.remove(num)
                seen.add(num)
                while (num + current_max) in unique_nums:
                    # unique_nums.remove(num+current_max)
                    seen.add(num+current_max)
                    current_max += 1
                if current_max > global_max:
                    global_max = current_max
        
        return global_max
                

