class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        for i in range(len(haystack)-len(needle)+1):
            index = 0
            start = i
            while haystack[start] == needle[index]:
                index += 1
                start += 1
                if index == len(needle):
                    return i
  
        
        return -1