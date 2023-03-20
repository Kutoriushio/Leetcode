class Solution:
    def countAndSay(self, n: int) -> str:      
        string = '1'
        for i in range(n-1):
            count = 0
            temp = ''
            let = string[0]          
            for j in range(0, len(string)):
                if string[j] == let:
                    count += 1
                else:
                    temp += str(count) + let
                    count = 1
                    let = string[j]
            temp += str(count) + let
            string = temp
        return string


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            base = '1'
            return base
        
        string = self.countAndSay(n-1)
        res = ''
        count = 0
        temp = string[0]
        for i in range(0, len(string)):
            if string[i] == temp:
                count += 1
            else:
                res += str(count) + temp
                count = 1
                temp = string[i]
        res += str(count) + temp
        return res