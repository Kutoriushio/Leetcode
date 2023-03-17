# Solution(Python)

## Dynamic programing TC(O(N)) SC(O(N))

1. A valid decode result belongs to one of the following two categories:

- Category 1: ending with a valid one-digit (for example: [........, 9] or [.........., 2])
- Category 2: ending with a valid two-digit (for example: [........, 12] or [........, 20] or [........, 16] )

2. Because each valid decode result is in either Category 1 or 2, we have 4 cases:

- Category 1 to Category 1 (for example: [........, 9] --add X--> [........, 9, X])
- Category 1 to Category 2 (for example: [........, 2] --add X--> [........, 2X])
- Category 2 to Category 1 (for example: [........, 20] --add X--> [........, 20, X])
- Category 2 to Category 2 is Impossible. (for example: [........, 21] --cannot change into-- > [........, 2, 1X])

3. Since both Category 1 and 2 can be changed into Category 1, therefore,

- count1 = previous count1 + previous count2

4. Only Category 1 can be changed into Category 2, therefore,

- count2 = previous count1