class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(1, numRows+1):
            temp = []
            for j in range(i):
                if j == 0:
                    temp.append(1)
                elif j == i - 1:
                    temp.append(1)
                else:
                    temp.append(res[-1][j-1] + res[-1][j]) # calculate current line from previous line
            res.append(temp)
        return res
