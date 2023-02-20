class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums) + 1
        money = [0] * n
        money[1] = nums[0]
        for i in range(2, n):
            money[i] = max(money[i-2] + nums[i-1], money[i-1])
        return money[-1]