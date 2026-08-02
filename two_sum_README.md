# Two Sum

**Difficulty:** Easy

**Problem:** Given a list of numbers and a target value, find the two 
numbers that add up to the target and return their indices.

**Approach:** Used a hashmap (`seen`) to store each number and its index 
as we go through the list. For every number, check if its complement 
(target - number) already exists in the hashmap. If it does, we've 
found our pair.

**Time Complexity:** O(n)
**Space Complexity:** O(n)
