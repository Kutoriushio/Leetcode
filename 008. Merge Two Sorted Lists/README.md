# Solution(Python)

1. Define a new linked list, make two pointers `dummy` and `cur` point the head of it.

2. Compare the value of `list1` and `list2`, if `list1.val >= list2.val`, let the pointer `cur` point `list1` and vice versa.

3. After each comparing, the corresponding linked list move to next.

4. Iterate over two linked lists until one is empty, in each iteration let `cur` move to next.

5. After iteration, let `cur` point the rest of unempty linked list,`list1` or `list2`.

6. As `dummy` and `cur` point the same LinkedList, so the `dummy.next` will be the result.

