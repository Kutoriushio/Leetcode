class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits) - 1
        while digits[length] == 9:
            digits[length] = 0
            l -= 1
        if l < 0:
            digits = [length] + digits
        else:
            digits[length] += 1
        return digits