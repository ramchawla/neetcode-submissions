class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # set our pointers -> 
            # target is inside nums so start and end
        # what are we returning ->
            # return index of target 
        # what function gives us the binary decision ->
            # whether mid point == target
        
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1
