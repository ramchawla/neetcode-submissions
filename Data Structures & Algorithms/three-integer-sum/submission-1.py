class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # use two pointer approach 
        # find sum of i + j
        # iterate over the list to look for a match
        # exclude the values at i and j
        # if found, create a sorted list containing the values
        # add this list object to our set
        # increment i and j

        ans = []
        n = len(nums) - 1
        i, j = 0, n
        while i < n:
            curr_sum = nums[i] + nums[j]
            target = 0 - curr_sum
            for k in range(len(nums)):
                if (k != i and k!= j and nums[k] == target):
                    sorted_lst = [nums[i], nums[j], nums[k]]
                    sorted_lst.sort()
                    if sorted_lst not in ans:
                        ans.append(sorted_lst)
                
            if j - i > 1:
                j -= 1
            else:
                j = n
                i += 1


        return ans