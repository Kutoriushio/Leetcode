# Solution(Python)

## TC(O(m*n)) SC(O(m*n))

1. Traverse the matrix, find the `O` that is next to the boarder.

2. Then search the element near the `O` recrusively.

3. Change them to `A`.

4. Finally change all the `O` to `X`, `A` to `O`.

