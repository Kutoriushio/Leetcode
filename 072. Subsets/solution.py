class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res += [[num] + cur for cur in res]
        
        return res


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(first, path):
            if len(path) == k:
                res.append(path[:])
            
            for i in range(first, n):
                path.append(nums[i])
                dfs(i+1, path)
                path.pop()
        
        n = len(nums)
        res = []
        path = []
        for k in range(n+1):
            dfs(0, path)
        
        return res