# Solution (Python)

## BFS
1. We put our root into queue, now we have level 0 in our queue.
2. On each step extract all nodes from queue and put their children to to opposite end of queue. In this way we will have full level in the end of each step and our queue will be filled with nodes from the next level.
3. In the end we just return result.

## DFS

1. Use `depth` to record the depth of the tree.

2. Add a new list that holds all nodes at that depth, when traversing to a new depth.

3. In the end we just return result.