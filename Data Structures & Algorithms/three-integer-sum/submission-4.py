class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # use 2 pointer approach - fix the first element
        # sort the input and then put pointers on opposite ends
        # similar to 2Sum, reduce r if too big and reduce l if
        # too small, but in order to keep space complexity as O(1)
        # we need to explicitly skip duplicates along the way
        ans = []
        nums.sort()

        for i, anchor in enumerate(nums):
            if anchor > 0:
                break # return early bc all positives ≠ 0
            
            if i > 0 and anchor == nums[i - 1]:
                continue # skip if a is duplicate
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = anchor + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    ans.append([anchor, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        
        return ans

        
                

                
                
            
