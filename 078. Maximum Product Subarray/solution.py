class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -math.inf
        max_num = 1
        min_num = 1
        for num in nums:
            if num < 0:
                temp = max_num
                max_num = min_num
                min_num = temp
            max_num = max(max_num * num, num)
            min_num = min(min_num * num, num)
            res = max(max_num, res)
        
        return res