def sum_even_numbers(number):
    total=0
    for num in number:
        if num%2==0:
            total+=num
    return total
n=int(input("Enter how many numbers: "))
number=[]
for i in range(n):
    num=int(input(f"Enter number{i+1}: "))
    number.append(num)
print("Input:",number)
print("Sum of even numbers: ",sum_even_numbers(number))        