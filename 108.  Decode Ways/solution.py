class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            count1 = [0]
        else:
            count1 = [1]
        count2 = [0]
        for i in range(1, len(s)):
            if s[i] == '0':
                count1.append(0)
            else:
                count1.append(count1[i-1] + count2[i-1])
            if '10' <= s[i-1] + s[i] <= '26':
                count2.append(count1[i-1])
            else:
                count2.append(0)
        
        return count1[-1] + count2[-1]