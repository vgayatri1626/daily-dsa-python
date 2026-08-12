# Move Zeroes

**Difficulty:** Easy

**Problem:** Given an array of numbers, move all zeroes to the end 
while maintaining the relative order of the non-zero elements.

**Approach:** Used the **Two Pointers** technique. A pointer `pos` 
tracks where the next non-zero element should go. As we scan through 
the array, whenever we find a non-zero element, we swap it into 
position `pos` and increment `pos`. This naturally pushes all zeroes 
toward the end without needing extra space.

**Time Complexity:** O(n)
**Space Complexity:** O(1)
