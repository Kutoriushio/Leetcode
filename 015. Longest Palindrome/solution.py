class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        count = 0
        for i in dic.values():
            rem = i % 2
            count += i - rem
        if count < len(s):
            count += 1
        return count