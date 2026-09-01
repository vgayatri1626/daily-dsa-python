def reverse_number(num):
    r=0
    while num>0:
        digit=num%10
        r=r*10+digit
        num//=10
    return r
num=int(input("Enter the number: "))
print("Reversed number: ",reverse_number(num))
    
