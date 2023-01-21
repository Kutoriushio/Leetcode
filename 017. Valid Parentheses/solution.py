class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        dic = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        stack = []
        for i in s:
            if i in dic:
                if  stack == [] or stack[-1] != dic[i]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(i)
        
        return not stack