from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 3 cases to check:
        # check for duplicates in row
        # check for duplicates in column
        # check for duplicates in square
        # for square, use floor division and tuple at key of dict
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == ".":
                    continue
                if ( board[r][c] in row[r]
                    or board[r][c] in col[c]
                    or board[r][c] in square[(r // 3, c // 3)]):
                    return False
                
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                square[(r // 3, c // 3)].add(board[r][c])

        
        return True


    
        
