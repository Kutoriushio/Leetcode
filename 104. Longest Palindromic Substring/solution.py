class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        length = 1
        start = 0
        for i in range(n):
            dp[i][i] = True
        for L in range(2, n+1):
            for i in range(n):
                j = i + L - 1
                if j > n - 1:
                    break
                if s[i] == s[j]:
                    if L == 2:
                        dp[i][j] = True
                    elif dp[i+1][j-1] == True:
                        dp[i][j] = True

                if dp[i][j] == True and L > length:
                    length = L
                    start = i
        
        return s[start:start+length]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = 1
        start = 0
        end = 0
        for i in range(n):
            length = 1
            left = i - 1
            right = i + 1
            while right < n and s[right] == s[i]:
                length += 1
                right += 1
            while left >= 0 and right < n and s[left] == s[right]:
                length += 2
                left -= 1
                right += 1
            if length > res:
                res = length
                start = left + 1
        
        return s[start:start+res]