def second_largest(number):
    largest=float('-inf')
    second=float('-inf')
    for nums in number:
        if nums>largest:
            second=largest
            largest=nums
        elif nums>second and nums!=largest:
            second=nums
    return second            
n=int(input("Enter how many numbers: "))
number=[]
for i in range(n):
    num=int(input(f"Enter number{i+1}: "))
    number.append(num)
print("Input: ",number)
print("Second largest: ",second_largest(number))     