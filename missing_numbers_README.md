##Day 13 – Find the Missing Number-python##

## Problem Statement ##

Given an array containing "n" distinct numbers from "0" to "n", 
find the one missing number.

## Approach ##

Use the sum formula to find the expected sum of numbers from "0" to "n".
Calculate the actual sum of the elements in the array and subtract it from
the expected sum. The difference gives the missing number.

## Complexity Analysis ##

- Time Complexity: "O(n)"
- Space Complexity: "O(1)"
