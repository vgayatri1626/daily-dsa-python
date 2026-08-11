Day 10 – Longest Substring Without Repeating 
Characters

##Problem Statement##

Given a string, find the length of the longest 
substring without repeating characters.

##Approach##

Use the Sliding Window technique with a Set.
Two pointers, "left" and "right", are used to 
maintain the current window. When a duplicate
character is found, characters are removed from 
the left until the duplicate is removed. The maximum
window length is then tracked.

##Complexity Analysis##

- Time Complexity: "O(n)"
- Space Complexity: "O(n)"
