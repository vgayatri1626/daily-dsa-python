n=int(input("Enter how many numbers: "))
number=[]
for i in range(n):
    num=int(input(f"Enter number{i+1}: "))
    number.append(num)
t=int(input("Enter the target sum: ")) 
seen={}
result=None
for i in range(len(number)):
    c=t-number[i]
    if c in seen:
        result=[seen[c],i]
        break
    seen[number[i]]=i
if result:
    print("Indices: ",result)
    print(f"{number[result[0]]} + {number[result[1]]} = {t}")
else:
    print("No two numbers add up to the target.")           