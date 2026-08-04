s1=input("Enter first word: ")
s2=input("Enter second word: ")
count_s1={}
for char in s1:
    count_s1[char]=count_s1.get(char,0)+1
count_s2={}
for char in s2:
    count_s2[char]=count_s2.get(char,0)+1
if count_s1==count_s2:
    print("Result: TRUE ")
else:
    print("Result: FALSE ")            
