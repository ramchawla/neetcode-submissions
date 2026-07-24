class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # iterate over nums
        # initialize a tmp array to be equal to nums
        # on each iteration, pop the current element
        # find the product of tmp
        # append that to output
        output = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if j == i:
                    continue
                product *= nums[j]
            output.append(product)
        
        return output
