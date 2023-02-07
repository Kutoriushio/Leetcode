class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        two = len(nums) - 1
        i = 0
        while i <= two:
            if nums[i] == 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[i], nums[two] = nums[two], nums[i]
                two -= 1 # We dont know swaped number, so we need  to check it in next loop.