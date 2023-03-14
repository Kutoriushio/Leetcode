class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(path, left, right):
            if len(path) == 2*n:
                res.append(''.join(path))
                return
            
            if left < n:
                path.append('(')
                backtrack(path, left+1, right)
                path.pop()
            
            if right < left:
                path.append(')')
                backtrack(path, left, right+1)
                path.pop()

        path = []
        res = []
        backtrack(path, 0, 0)
        return res