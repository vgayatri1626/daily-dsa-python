def longest_substring(s):
    c=set()
    left=0
    maxlength=0
    for right in range(len(s)):
        while s[right]in c:
            c.remove(s[left])
            left+=1
        c.add(s[right])
        maxlength=max(maxlength,right-left+1)
    return maxlength        
text=input("Enter the string: ")
print("Longest string length: ",longest_substring(text))    