class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        right = len(s) - 1
        left = 0
        while left < right:
            temp = s[right]
            s[right] = s[left]
            s[left] = temp
            right -= 1
            left += 1