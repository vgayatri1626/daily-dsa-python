def reverse_string(s):
    s=list(s)
    left=0
    right=len(s)-1
    while left<right:
        s[left],s[right]=s[right],s[left]
        left+=1
        right-=1
    return " ".join(s)
text=input("Enter a string: ")
print("REVERSE STRING: ",reverse_string(text))
    