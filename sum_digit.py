def sum_digit(num):
    t=0
    while num>0:
        digit=num%10
        t+=digit
        num//=10
    return t
num=int(input("Enter a number: "))
print("Sum of digits: ",sum_digit(num))    
