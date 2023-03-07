class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = set()
        left = 0
        cur = 0
        res = 0
        for i in range(len(s)):
            cur += 1
            while s[i] in sub:
                sub.remove(s[left])
                left += 1
                cur -= 1
            res = max(res, cur)
            sub.add(s[i])

        return res


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = {}
        left = 0
        res = 0
        j = 0
        for i in range(len(s)):
            if s[i] in sub:
                j = max(sub[s[i]], j)
            
            res = max(res, i-j+1)
            sub[s[i]] = i + 1

        return res