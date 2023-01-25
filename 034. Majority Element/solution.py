# HashMap
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
            if dic[num] > len(nums) / 2:
                return num


# Boyer-Moore Voting
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None # Initialize candidate
        count = 0 
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1) # If in the same camp as the candidate, count + 1
        
        return candidate