# Solution(Python)

## TC(O(N)) SC(O(N))

1. If an operand is encountered, the operand is placed on the stack.

2. If an operator is encountered, the two operands are taken off the stack, where the first one is the right operand and the second one is the left operand. The two operands are operated on using the operator and the new operand obtained by the operation is put on the stack.