def missing_number(number):
    nums=len(number)
    exp_sum=nums*(nums+1)//2
    act_sum=sum(number)
    return exp_sum - act_sum
n=int(input("Enter how many numbers: "))
number=[]
for i in range(n):
    num=int(input(f"Enter number{i+1}: "))
    number.append(num)
print("Input: ",number)
print("Missing Number: ",missing_number(number))    