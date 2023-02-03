class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, res, path, used, depth):
            if depth == len(nums):
                return res.append(path[:])
            
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    dfs(nums, res, path, used, depth+1)
                    
                    used[i] = False
                    path.pop()
        
        res = []
        path = []
        used = [False for _ in range(len(nums))]
        depth = 0
        dfs(nums, res, path, used, depth)
        return res