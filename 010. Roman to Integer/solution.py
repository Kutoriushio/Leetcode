# Solution 1:
class Solution:
    def romanToInt(self, s: str) -> int:
        s = s.replace('IV','IIII').replace('IX','VIIII')
        s = s.replace('XL', 'XXXX').replace('XC','LXXXX')
        s = s.replace('CD', 'CCCC').replace('CM','DCCCC')
        count = 0
        for i in s:
            if i == 'I':
                count += 1
            elif i == 'V':
                count += 5
            elif i == 'X':
                count += 10
            elif i == 'L':
                count += 50
            elif i == 'C':
                count += 100
            elif i == "D":
                count += 500
            elif i == "M":
                count += 1000
        
        return count

# Solution 2:
class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        result = 0
        biggest = 0
        for i in s[::-1]:
            temp = dic[i]
            if temp >= biggest:
                result += temp
                biggest = temp
            else:
                result -= temp
        
        return result