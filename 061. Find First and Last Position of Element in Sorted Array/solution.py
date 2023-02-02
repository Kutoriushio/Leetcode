# TC(O(log(N))) SC(O(1))
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        # find the first position
        left = 0
        right = len(nums) - 1
        res = []
        while left < right:
            mid = (left+right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        # when jump out the loop, left pointer always point the first position
        if nums[left] == target:
            res.append(left)
        left = 0
        right = right = len(nums) -1
        # Find the last position
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        # when jump out the loop, right pointer always point the last position
        if nums[right] == target:
            res.append(right)
        if res:
            return res
        else:
            return [-1, -1]
