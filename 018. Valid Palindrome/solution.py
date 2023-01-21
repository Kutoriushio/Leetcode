class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        temp = ''

        for i in s:
            if i.isdigit() or i.isalpha():
                temp += i

        left = 0
        right = len(temp) - 1
        if len(temp) == 0:
            return True
        while right >= left:
            if temp[right] != temp[left]:
                return False
            left += 1
            right -= 1
        return True