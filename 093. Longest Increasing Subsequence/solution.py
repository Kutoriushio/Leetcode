class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j]+1, dp[i])
        
        return max(dp)


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        sub = []
        for num in nums:
            if len(sub) == 0 or sub[-1] < num:
                sub.append(num)
            else:
                left = 0
                right = len(sub) - 1
                while left < right:
                    mid = (left + right) // 2
                    if sub[mid] < num:
                        left = mid + 1
                    else:
                        right = mid
                sub[left] = num
        
        return len(sub)