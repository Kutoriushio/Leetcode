class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n = len(nums)
        temp = [0] * n
        end = n - 1
        for i in range(1, n, 2):
            temp[i] = nums[end]
            end -= 1
        for i in range(0, n, 2):
            temp[i] = nums[end]
            end -= 1
        for i in range(n):
            nums[i] = temp[i]