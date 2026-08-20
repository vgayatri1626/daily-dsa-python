## Day 17 – GCD of Two Numbers ##

## Problem Statement ##

Given two positive integers, find their Greatest Common Divisor (GCD), 
which is the largest number that divides both numbers without leaving a remainder.

## Approach ##

Use the Euclidean Algorithm.

Repeatedly find the remainder of the two numbers and replace the larger number
with the smaller number until the remainder becomes "0". The remaining number is the GCD.

## Complexity Analysis ##

- Time Complexity: "O(log(min(a, b)))"
- Space Complexity: "O(1)"
