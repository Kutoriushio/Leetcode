class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        flag = [[True for _ in range(n)] for _ in range(m)]
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        used = []
        def search(i,j):
            used.append((i,j))
            for direction in directions:
                di = i + direction[0]
                dj = j + direction[1]
                if (di,dj) not in used:
                    if 0 <= di <= m-1 and 0 <= dj <= n-1:
                        if board[di][dj] == 'O':
                            flag[di][dj] = False
                            search(di,dj)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    flag[i][j] = False
                if board[i][j] == 'O':
                    if i == 0 or i == m -1 or j == 0 or j == n - 1:
                        flag[i][j] = False
                        search(i,j)
        
        for i in range(m):
            for j in range(n):
                if flag[i][j]:
                    board[i][j] = 'X'