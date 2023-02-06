# Solution(Python)

## Solution1 TC(O(MN)) SC(O(MN))

1. We make a pass over our original array and look for zero entries.

2. If we find that an entry at `[i, j]` is 0, then we need to record somewhere the row i and column j.

3. We use two lists, one for the rows and one for the columns.

4. Finally, we iterate over the original matrix. For every cell we check if the row  or column  had been marked earlier. If any of them was marked, we set the value in the cell to 0.

## Solution2 TC(O(MN)) SC(O(1))

1. We can use the first row and column of the matrix instead of the two tag arrays in solution 1

2. We need to use two additional marker variables to record whether the first row and column originally contained 0.