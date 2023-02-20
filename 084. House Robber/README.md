# Solution(Python)

## TC(O(N)) SC(O(1))

- M(k) = money at the kth house
- P(0) = 0
- P(1) = M(1)
- P(k) = max(P(k−2) + M(k), P(k−1))