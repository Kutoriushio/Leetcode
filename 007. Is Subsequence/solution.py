class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        i = 0
        length = len(t)
        while i < length and index < len(s):
            if s[index] == t[i]:
                index += 1
            i += 1
        
        return index == len(s)