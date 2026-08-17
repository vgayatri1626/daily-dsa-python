## Day 14 – Second Largest Element-python ##

## Problem Statement ##

Given an array of integers, find the second largest
distinct element in the array.

## Approach ##

Use two variables, "largest" and "second_largest".

Traverse the array and update them whenever a larger or second-largest value is found. This allows us to find the second largest element in a single pass without sorting the array.

## Complexity Analysis ##

- Time Complexity: "O(n)"
- Space Complexity: "O(1)"
