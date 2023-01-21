class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for i in s:
            dic[i] = dic.get(i,0) + 1
        for index, ch in enumerate(s):
            if dic[ch] == 1:
                return index
        
        return -1