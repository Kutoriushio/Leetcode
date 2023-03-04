# Solution(Python)

## TC(O(1)) SC(O(N))

### Insert
- add the element to the dictionary. Setting the value as the length of the list will accurately point to the index of the new element. `(len(some_list) is equal to the index of the last item +1)`

### Remove

1. Move the last element in the list into the location of the element we want to remove. 

2. Change the last element in the list to now be the value of the element.

3. Remove the last element in the list.

4. Remove the element to be removed from the dictionary

### Random

1. Randomly select an element from the list of data.