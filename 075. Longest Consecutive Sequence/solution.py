class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_seq = 0
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        cur_stack = 1
        if len(nums) == 1:
            return len(nums)
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                cur_stack += 1
            else:
                cur_stack = 1
            
            longest_seq = max(cur_stack, longest_seq)
        return longest_seq

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_seq = 0
        nums.sort()
        cur_stack = 1
        if len(nums) == 1:
            return len(nums)
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                cur_stack += 1
            elif nums[i+1] == nums[i]:
                pass
            else:
                cur_stack = 1
            
            longest_seq = max(cur_stack, longest_seq)
        return longest_seq

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for num in nums:
            cur = 1
            if num - 1 not in nums:
                while num + 1 in nums:
                    num += 1
                    cur += 1
                
                longest = max(cur, longest)
        
        return longest