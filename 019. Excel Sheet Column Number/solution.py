class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        digit = 0
        count = 0
        length = len(columnTitle)
        for i in range(length-1, -1, -1):
            count += (ord(columnTitle[i]) - 64) * (26 ** digit)
            digit += 1
        return count