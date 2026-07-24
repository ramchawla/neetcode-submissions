class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area = length x width
        # length = min(heights[l], heights[r])
        # width = r - l
        # store current max and global max
        l, r = 0, len(heights) - 1
        length, width = 0, 0
        currA, maxA = 0, 0
        while l < r:
            length = min(heights[l], heights[r])
            width = r - l
            currA = length * width
            maxA = max(maxA, currA)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxA

