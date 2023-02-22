# Solution(Python)

## TC(O(NlogNlogN)) SC(O(N))

### The Sieve of Eratosthenes
1. Initial length N tagged array indicating whether this number is prime or not. The array initializes all numbers to be prime.

2. All multiples of the current number from 2 onwards are marked as a composite. Marking up to `sqrt(n)` then stop.

3. Each time you find a multiple of the current prime x, start with `x^2`.