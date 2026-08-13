##Day 12 – Product of Array Except Self-python##

##Problem Statement##

Given an integer array, return an array where each
element is the product of all elements in the original
array except the element at the current index.

##Approach##

. Use prefix and suffix products.
. First, calculate the product of all 
elements to the left of each index.
. Then, calculate the product of
all elements to the right and multiply
it with the prefix product.
. This avoids using division and handles
zero values correctly.

##Complexity Analysis##

Time Complexity: O(n)
Space Complexity: O(1) (excluding the output array)
