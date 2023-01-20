class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        length = 500
        for i in strs:
            length = min(length,len(i))
        
        for i in range(length):
            temp = ''
            for j in strs:
                temp += j[i]
            temp = set(temp)
            if len(temp) != 1:
                return res
            else:
                res += ','.join(temp)
        
        return res