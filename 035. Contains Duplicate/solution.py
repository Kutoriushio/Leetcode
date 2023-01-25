
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums) # set can remove duplicate elements


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1 
            if dic[num] >= 2:
                return True
        
        return False