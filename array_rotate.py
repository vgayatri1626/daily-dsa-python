def rotate_array(number,l):
    l = l %len(number)
    return number[-l:] + number[:-l]
l=int(input("Enter the number of rotation: "))
n=int(input("Enter how many numbers: "))
number=[]
for i in range(n):
    num=int(input(f"Enter number{i+1}: "))
    number.append(num)
print("Input: ",number)
print("Rotated Array: ",rotate_array(number,l))     
