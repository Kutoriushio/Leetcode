# sort
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0,len(nums)):
            if i != nums[i]:
                return i
        
        return len(nums)

# xor
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        for i, num in enumerate(nums):
            xor ^= i ^ num
        
        return xor^len(nums)

# math
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = sum(nums)
        total = (len(nums) * (len(nums)+1)) // 2
        return total - s

# hash 
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = set(nums)
        for i in range(0, len(nums)+1):
            if i not in s:
                return i