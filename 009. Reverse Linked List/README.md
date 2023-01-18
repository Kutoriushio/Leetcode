# Solution(Python)

Assume there is a linked list like this `1 → 2 → 3 → 4 → 5`, need to reverse it.

1. `None`  `1 → 2 → 3 → 4 → 5`  
&nbsp;&nbsp;pre&nbsp;&nbsp;&nbsp;cur
2. `None ← 1` `2 → 3 → 4 → 5`    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pre&nbsp;cur
3. `None ← 1 ← 2` `3 → 4 → 5`     
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pre&nbsp;cur
4. `None ← 1 ← 2 ← 3` `4 → 5`   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pre&nbsp;cur
5. `None ← 1 ← 2 ← 3 ← 4` `5`    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pre&nbsp;cur
6. `None ← 1 ← 2 ← 3 ← 4 ← 5`    
