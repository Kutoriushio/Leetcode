# Solution(Python)

## TC(O(log(N))) SC(O(1))

The array is divided into two, one of which must be sorted, and the other may be sorted or partially ordered.
At this point the ordered part is found using the dichotomy method. The unsorted part is then divided into two, one of which must be sorted, the other may be sorted and the other may be unsorted. This is how the cycle works.

