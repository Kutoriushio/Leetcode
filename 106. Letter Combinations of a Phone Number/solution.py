class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        n = len(digits)
        if n == 0:
            return res
        dic = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        def dfs(i, path):
            if len(path) == n:
                res.append(''.join(path))
                return
            digit = digits[i]
            letters = dic[digit]
            for letter in letters:
                path.append(letter)
                dfs(i+1, path)
                path .pop()
            
        path = []
        dfs(0, path)
        return res