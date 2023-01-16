class Solution:
    def pivotIndex(self, nums):
        s = sum(nums)
        leftsum = 0
        for index, num in enumerate(nums):
            if leftsum == s - leftsum - num:
                return index
            leftsum += num
        
        return -1