class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -math.inf
        max_num = 1
        min_num = 1
        for num in nums:
            maxN = max_num
            minN = min_num
            max_num = max(maxN * num, num, minN * num)
            min_num = min(minN * num, num, maxN * num)
            res = max(max_num, res)
        
        return res