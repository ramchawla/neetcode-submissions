class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # we're given sorted input
        # we're looking for 2 elems
        # the relationship is global, not local
        # perfect setup for using 2 pointer approach
        # left pointer at start and right pointer at end
        # if sum if greater than target, reduce the larger pointer
        # if sum if smaller than target increase the smaller pointer

        l, r = 0, len(numbers) - 1
        ans = []

        while l <= r:
            curr = numbers[l] + numbers[r]

            if curr < target:
                l += 1
            elif curr > target:
                r -= 1
            else:
                ans.append(l+1)
                ans.append(r+1)
                break
        
        return ans
