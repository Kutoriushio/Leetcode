class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        res = 0
        while left < right:
            square = min(height[left], height[right]) * (right-left)
            res = max(res, square)
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
        return res