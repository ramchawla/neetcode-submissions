from collections import deque

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # left sums + right sums
        left = []
        right = deque()
        i = 0
        ans = []
        while i < len(nums):
            if i == 0:
                left.append(1)
                i += 1
                continue
            num = left[-1] * nums[i-1] # 1 *1
            left.append(num)
            i += 1
        
        j = -1
        while j >= (-1 * len(nums)):
            if j == -1:
                right.appendleft(1)
                j -= 1
                continue
            num = right[0] * nums[j + 1]
            right.appendleft(num)
            j -= 1
        
        for k in range(len(nums)):
            num = left[k] * right[k]
            ans.append(num)

        return ans
            
