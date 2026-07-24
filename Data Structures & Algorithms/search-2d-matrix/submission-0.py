class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # where are our pointers ->
            # looking for element within so each pointer can be at ends of the matrix
        # what do we need to return
            # boolean of contains
        # what is our binary function?
            # comparing mid point in the matrix
        # first find the row using incremental property
        start, end = 0, len(matrix) - 1
        while start <= end:
            middle = (start + end) // 2
            if target < matrix[middle][0]:
                end = middle - 1
            elif target > matrix[middle][-1]:
                start = middle + 1
            else:
                break
        
        # now we know which row contains the target
        if not (start <= end):
            return False
        row = (start + end) // 2
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True

        return False


         