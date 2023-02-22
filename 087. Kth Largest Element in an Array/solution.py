class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        target = n - k
        left = 0
        right = n-1
        def partition(nums, start, end):
            left = start
            right = end
            randomIndex = random.randint(left, right)
            nums[left], nums[randomIndex] = nums[randomIndex], nums[left]
            pivot = nums[left]
            while left < right:
                while nums[right] > pivot and left < right:
                    right -= 1
                nums[left] = nums[right]
                while nums[left] <= pivot and left < right:
                    left += 1
                nums[right] = nums[left]
            nums[left] = pivot
            return left
        while True:
            index = partition(nums, left, right)
            if index == target:
                return nums[index]
            if index < target:
                left = index + 1
            if index > target:
                right = index - 1