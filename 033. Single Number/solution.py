class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res ^= nums[i] # as repeat element onlyappears twice, 0^0=0，it will be 0 after xor,and 0^1 = 1
        return res