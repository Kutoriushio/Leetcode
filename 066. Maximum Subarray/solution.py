class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        max_subarray = 0
        for i in range(len(nums)):
            max_subarray = max(max_subarray+nums[i], nums[i])
            res = max(res, max_subarray)
        return res