class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
        def search(i, j, count):
            for direction in directions:
                di = direction[0]
                dj = direction[1]
                new_i = i + di
                new_j = j + dj
                if 0 <= new_i <= m -1 and 0 <= new_j <= n - 1:
                    if board[new_i][new_j] == 1 or board[new_i][new_j] == '1':
                        count += 1
            return count
        for i in range(m):
            for j in range(n):
                count = 0
                if board[i][j] == 0:
                    count = search(i, j, count)
                    if count == 3:
                        board[i][j] = '0'
                else:
                    count = search(i, j, count)
                    if count < 2:
                        board[i][j] = '1'
                    elif count > 3:
                        board[i][j] = '1'
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == '1':
                    board[i][j] = 0
                if board[i][j] == '0':
                    board[i][j] = 1