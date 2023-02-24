class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            cur = abs(num)
            if nums[cur] < 0:
                return cur
            nums[cur] = -nums[cur]

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = 1
        right = len(nums) - 1
        duplicate = 0
        while left <= right:
            count = 0
            mid = (left + right) // 2
            for num in nums:
                if num <= mid:
                    count += 1
            if count > mid:
                duplicate = mid
                right = mid - 1
            else:
                left = mid + 1
        return duplicate

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        temp = nums[0]
        while temp != slow:
            temp = nums[temp]
            slow = nums[slow]
        return slow