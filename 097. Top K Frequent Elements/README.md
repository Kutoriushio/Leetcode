# Solution(Python)

## Heap TC(O(NlogK)) SC(O(N))
1. Use a hash table to count the frequencies.

2. Create a heap, return the k largest keys of the hash table.


## Bucket Sort TC(O(N)) SC(O(N))
1. Use a hash table to count the frequencies.

2. Once the count is complete, create an array and use the frequencies as subscripts for the array, and for sets of numbers that occur with different frequencies, just store them in the corresponding array subscripts.

3. Start traversing from the end and append the num until the length of `res` is k.