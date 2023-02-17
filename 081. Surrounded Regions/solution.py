class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        def search(i,j):
            for direction in directions:
                di = i + direction[0]
                dj = j + direction[1]
                if 0 <= di <= m-1 and 0 <= dj <= n-1:
                    if board[di][dj] != 'A':
                        if board[di][dj] == 'O':
                            board[di][dj] = 'A'
                            search(di,dj)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    if i == 0 or i == m -1 or j == 0 or j == n - 1:
                        board[i][j] = 'A'
                        search(i,j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'A':
                    board[i][j] = 'O'