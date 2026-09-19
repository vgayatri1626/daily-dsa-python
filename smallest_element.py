def find_smallest(nums):
    smallest=nums[0]
    for num in nums:
        if num<smallest:
            smallest=num
    return smallest
nums=[10,20,4,3,1,76]
print("Input: ",nums)
print("Smallest Element: ",find_smallest(nums))        