# Sotuion(Python)

## TC O(Nlog(N)) SC O(log(N))

1. Sorted by the left endpoint of the interval.

2. Add the first interval to the `res` array.

3. If the left endpoint of the current interval is after the right endpoint of the last interval in the array `res`, then they do not overlap and we can simply add this interval to the end of the array `res`.

4. Otherwise, they overlap and we need to update the right endpoint of the last interval in the `res` array with the right endpoint of the current interval, setting it to the greater of the two.