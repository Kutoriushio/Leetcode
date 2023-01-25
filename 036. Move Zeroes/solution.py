class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        index = 0
        for num in nums:
            if num != 0:
                nums[index] = num # put non-zero numbers into a list in order
                index += 1
        for i in range(index,  length):
            nums[i] = 0 # put zeros into the rest of the list