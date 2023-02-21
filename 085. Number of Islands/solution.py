class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        def dfs(grid, i, j):
            if 0 <= i <= m - 1 and 0 <= j <= n - 1 and grid[i][j] == '1':
                grid[i][j] = 'A'
                dfs(grid, i+1, j)
                dfs(grid, i-1, j)
                dfs(grid, i, j+1)
                dfs(grid, i, j-1)


        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(grid, i, j)

        return count


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        def bfs(grid, i, j):
            queue = [[i,j]]
            while queue:
                [i,j] = queue.pop(0)
                if 0 <= i <= m - 1 and 0 <= j <= n - 1 and grid[i][j] == '1':
                    grid[i][j] = 'A'
                    queue += [[i+1,j], [i-1,j], [i,j+1], [i,j-1]]


        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    bfs(grid, i, j)

        return count
