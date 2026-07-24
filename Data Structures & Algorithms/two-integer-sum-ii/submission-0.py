class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # use a double for loop approach 
        # need to keep track of indexes
        # need to increment index at the end to make it 1-indexed
    
        for i in range(len(numbers)):
            index1 = i
            for j in range(i+1, len(numbers)):
                index2 = j
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
                