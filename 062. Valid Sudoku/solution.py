class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[0]*9 for _ in range(9)] # create (9*9) list to store row numbers
        columns = [[0]*9 for _ in range(9)] # create (9*9) list to store column numbers
        boxes = [[[0]*9 for _ in range(3)] for _ in range(3)] # create (3*3*9) list to store box numbers
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num) - 1
                    # corresponding index + 1
                    rows[i][num] += 1 
                    columns[j][num] += 1
                    boxes[i//3][j//3][num] += 1
                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[i//3][j//3][num] > 1:
                        return False
        
        return True