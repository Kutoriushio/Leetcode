# Solution(Python)

## TC(O(MN)) SC(O(1))

1. Traverse all the cells in `board`.

2. Calculate the number of live cells in each cell's eight neighbors.

3. Accroding to the rules, change the state of cells. `1` represents that the cell was alive and is now dead, `0` represents that the cell was dead and is now alive.

4. Traverse all the cells in `board` again, change the state of cells.