def count_frequency(number):
    f={}
    for nums in number:
        if nums in f:
            f[nums]+=1
        else:
            f[nums]=1
    return f            
n=int(input("Enter how many numbers: "))
number=[]
for i in range(n):
    num=int(input(f"Enter number{i+1}: "))
    number.append(num)
print("Input: ",number)
print("Frequency: ",count_frequency(number))     