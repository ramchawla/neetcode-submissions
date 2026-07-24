class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # find product to the left, replace output array with those values
        # find product to the right, multiply output array by those
        # [1, 1, 2, 8] <- left product
        # [48, 24, 6, 1] <- right product
        output = [1] * len(nums)
        # [1, 1, 1, 1]

        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        
        # left product in place

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        
        return output