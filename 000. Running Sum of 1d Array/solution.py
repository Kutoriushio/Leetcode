class Solution:
    def runningSum(self, nums):
        ans = [nums[0]]
        l = len(nums)
        for i in range(1,l):
            ans.append(nums[i] + ans[i-1])

        return(ans)