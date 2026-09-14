def find_largest(nums):
    largest=nums[0]
    for num in nums:
        if num>largest:
            largest=num
    return largest   
nums=[10,11,17,13,24]
print("Input ",nums)
print("Largest Element: ",find_largest(nums))     