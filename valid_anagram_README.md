# Valid Anagram

**Difficulty:** Easy

**Problem:** Given two strings, check if they are anagrams of each 
other — meaning they contain exactly the same letters with the same 
frequency, just in a different order.

**Approach:** Built a dictionary to count how many times each letter 
appears in the first word, and another dictionary for the second word. 
If both dictionaries are identical, the words use the exact same 
letters in the same amounts, so they're anagrams.

**Time Complexity:** O(n)
**Space Complexity:** O(n)
