# Solution(Python)

# TC(O(N^2)) SC(O(1))

1. element at `(row,column)`, after rotation, it will be at `(column, n-row-1)`. We can get equation `(row, column) = (column, n-row-1)`.

2. For element at `(column, n-row-1)`, after rotation, accroding to the equation, it will be at `(n-row-1, n-column-1)`.

3. For element at `(n-row-1, n-column-1)`, after rotation, acrroding to the equation, it will be at `(n-column-1, row)`.

4. For element at `(n-column-1, row)`, after rotation, acrroding to the equation, it will be at `(row, column)`.