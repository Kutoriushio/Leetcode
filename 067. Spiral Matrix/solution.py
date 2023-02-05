class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0
        bottom = len(matrix)
        top = 0
        right = len(matrix[0])
        num = right * bottom
        res = []
        while num > 0:
            for i in range(left, right):
                if num > 0:
                    res.append(matrix[top][i])
                    num -= 1
            top += 1
            for i in range(top, bottom):
                if num > 0:
                    res.append(matrix[i][right-1])
                    num -= 1
            right -= 1
            for i in range(right-1, left-1,-1): 
                if num > 0:
                    res.append(matrix[bottom-1][i])
                    num -= 1
            bottom -= 1
            for i in range(bottom-1, top-1, -1):
                if num > 0:
                    res.append(matrix[i][left])
                    num -= 1
            left += 1
        return res