class Solution:
    def myAtoi(self, s: str) -> int:
        number = '0'
        max_number = 2 ** 31 - 1
        min_number = -2 ** 31
        start = 0
        flag = 1
        while start < len(s) and s[start] == ' ':
            start += 1
        if start == len(s):
            return 0
        if s[start] == '-':
            flag = -1
            start += 1
        elif s[start] == '+':
            flag = 1
            start += 1
        while start < len(s):
            if not s[start].isdigit():
                break
            number += s[start]
            start += 1
        res = flag * int(number)
        if res > max_number:
            return max_number
        elif res < min_number:
            return min_number
        else:
            return res


class Solution:
    def myAtoi(self, s: str) -> int:
        number = 0
        max_number = 2 ** 31 - 1
        min_number = -2 ** 31
        sign = 1
        flag = 0
        index = 0
        if len(s) == 0:
            return number
        while index < len(s):
            cur = s[index]
            if flag == 0:
                if cur == ' ':
                    flag = 0
                elif cur == '-':
                    sign = -1
                    flag = 1
                elif cur == '+':
                    sign = 1
                    flag = 1
                elif cur.isdigit():
                    flag = 2
                    number = number * 10 + int(cur)
                else:
                    return 0
            elif flag == 1:
                if cur.isdigit():
                    flag = 2
                    number = number * 10 + int(cur)
                else:
                    return 0
            elif flag == 2:
                if cur.isdigit():
                    flag = 2
                    number = number * 10 + int(cur)
                else:
                    break
            index += 1
        res = sign * number
        res = min(res, max_number)
        res = max(res, min_number)
        return res