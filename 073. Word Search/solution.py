class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m = len(board)
        n = len(board[0])
        def dfs(i, j, k):
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            visited[i][j] = 1
            result = False
            for di, dj in directions:
                new_i = i + di
                new_j = j + dj
                if 0 <= new_i < m and 0 <= new_j < n:
                    if visited[new_i][new_j] == 0:
                        if dfs(new_i, new_j, k+1):
                            result = True
                            break
            
            
            visited[i][j] = 0
            return result
        
        visited = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        
        return False