# Solution(Python)

## TC(O(MN3^L)) SC(O(MN))

1. If `board[i][j] != word[k]`, return `False`.

2. If the end of the string has been accessed and the corresponding character still matches, return `True`.

3. Otherwise, iterate through all adjacent positions of the current position.