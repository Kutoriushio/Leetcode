class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        pq = [(matrix[i][0], i, 0) for i in range(n)]
        heapq.heapify(pq)
        for i in range(k):
            res, row, col = heapq.heappop(pq)
            if col < n - 1:
                heapq.heappush(pq, (matrix[row][col+1], row, col+1))
        
        return res


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        left = matrix[0][0]
        right = matrix[n-1][n-1]
        def countMid(mid):
            col = n -1
            count = 0
            for row in range(n):
                while col >= 0 and matrix[row][col] > mid:
                    col -= 1
                count += col + 1
            return count
        while left < right:
            mid = (left + right) // 2
            count = countMid(mid)
            if count < k:
                left = mid + 1
            else:
                right = mid
        
        return left