class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # using 2 pointers on opposite ends
        # since we need to try every possible combination
        # we keep track of max so far and total max
        # area = length x width 
        # (min(l, r)) x (distance between l and r )
        # for each iteration, move in from the pointer than is smaller

        l, r = 0, len(heights) - 1
        highest = 0
        while l < r:
            highest_so_far = min(heights[l], heights[r]) * (r - l)
            if highest_so_far > highest:
                highest = highest_so_far
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return highest