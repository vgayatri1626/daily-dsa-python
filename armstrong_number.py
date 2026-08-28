def is_armstrong(num):
    digits=str(num)
    power=len(digits)
    total=sum(int(digit)**power for digit in digits)
    return total==num
num=int(input("Enter a number: "))
if is_armstrong(num):
    print(num,"is an armstrong number.")
else:
    print(num,"is not an armstrong number.")    