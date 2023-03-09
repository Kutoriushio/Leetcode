# Solution(Python)

## Backtracking TC(3^N*4^M) SC(M+N)

1. Use a hash table to store all possible letters corresponding to each number.

2. Perform backtracking operations.

- Maintain a list representing the existing alphabetical arrangement.

- The list is initially empty. One digit of the phone number is taken at a time, all possible letters corresponding to that digit are obtained from the hash table and one of them is inserted after the existing alphabetic arrangement.

- The next digit of the phone number is processed until all digits in the phone number have been processed, i.e. a complete alphabetic arrangement is obtained.

- After which a backtracking operation is performed, traversing the rest of the alphabetical arrangement