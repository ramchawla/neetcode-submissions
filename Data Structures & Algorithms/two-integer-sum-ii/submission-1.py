class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # use 2 pointer apprach
        # if sum > target, decrement right pointer
        # vice versa
        l, r = 0, len(numbers) - 1
        while True:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1

        
                