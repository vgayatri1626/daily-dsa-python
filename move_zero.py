def move_zero(nums):
    pos=0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[pos],nums[i]=nums[i],nums[pos]
            pos+=1
    return nums
nums=[0,1,1,0,2,3] 
print(move_zero(nums))       