class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            if i <= farthest:
                if farthest < nums[i] + i:
                    farthest = nums[i] + i

        return farthest >= len(nums) - 1