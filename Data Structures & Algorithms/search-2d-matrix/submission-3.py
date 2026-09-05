class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        b, t = 0, len(matrix) - 1
        row = []
        i = 0
        # do binary search to find row
        while b <= t:
            mid = (b + t) // 2
            if target > matrix[mid][-1]:
                b = mid + 1
            elif target < matrix[mid][0]:
                t = mid - 1
            else:
                row = matrix[mid]
                i = mid
                break
        
        # do binary search to find num
        l, r = 0, len(row) - 1

        while l <= r:
            m = (l + r) // 2
            if target > matrix[i][m]:
                l = m + 1
            elif target < matrix[i][m]:
                r = m - 1
            else:
                return True
        
        return False
        

        
