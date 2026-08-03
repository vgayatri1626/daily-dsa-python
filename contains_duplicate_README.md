# Contains Duplicate

**Difficulty:** Easy

**Problem:** Given a list of numbers, check if any value appears 
more than once in the list.

**Approach:** Used a `set` to track numbers as we go through the list. 
For each number, check if it's already in the set — if it is, we've 
found a duplicate and can stop immediately. If not, add it to the set 
and continue.

**Time Complexity:** O(n)
**Space Complexity:** O(n)
