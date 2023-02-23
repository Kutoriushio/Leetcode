class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1]
        suffix = [1]
        res = []
        for i in range(n-1):
            prefix.append(nums[i] * prefix[i])
            suffix.append(nums[n-i-1] * suffix[i])
        
        for i in range(n):
            res.append(prefix[i] * suffix[n-i-1])
        return res


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = 1
        suffix = 1
        res = [1] * n
        for i in range(n):
            res[i] *= prefix
            prefix *= nums[i]
        for i in range(n):
            res[n-i-1] *= suffix
            suffix *= nums[n-i-1]

        return res

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = 1
        suffix = 1
        res = [1] * n
        for i in range(n):
            res[i] *= prefix
            res[n-i-1] *= suffix
            prefix *= nums[i]
            suffix *= nums[n-i-1]
        return res