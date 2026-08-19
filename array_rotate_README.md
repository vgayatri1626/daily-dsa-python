🚀 Day 16 – Rotate Array

📌 Problem Statement

Given an array of integers, rotate the array to the right by "k" positions.

💡 Approach

Use array slicing to separate the last "k" elements and place them at the beginning.

- "nums[-k:]" gets the last "k" elements.
- "nums[:-k]" gets the remaining elements.
- Combine both parts to get the rotated array.
- Use "k % len(nums)" to handle rotations greater than the array length.

⏱️ Complexity Analysis

- Time Complexity: "O(n)"
- Space Complexity: "O(n)"
