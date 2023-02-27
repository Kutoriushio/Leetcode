class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = nums[0]
        second = math.inf
        for num in nums:
            if num > second:
                return True
            elif num <= first:
                first = num
            else:
                second = num
            
        
        return False