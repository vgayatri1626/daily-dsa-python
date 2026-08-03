n=int(input("Enter how many numbers: "))
number=[]
for i in range(n):
    num=int(input(f"Enter number{i+1}: "))
    number.append(num)
seen=set()
duplicate=False
for num in number:
    if num in seen:
        duplicate=True
        break
    seen.add(num)
if duplicate:
    print("Result: True(found)")
else:
    print("Result: False(not found)")   