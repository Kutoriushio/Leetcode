class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(x) for x in nums]
        for i in range(len(nums)):
            for j in range(0, len(nums)-i-1):
                if nums[j] + nums[j+1] < nums[j+1] + nums[j]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        if nums[0] == '0':
            return '0'
        else:
            return ''.join(nums)