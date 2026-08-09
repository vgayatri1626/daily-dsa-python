def vowels_consonants(s):
    vowels=0
    consonants=0
    for char in s.lower():
        if char in "aeiou":
            vowels+=1
        elif char.isalpha():    
            consonants+=1
    return vowels,consonants            
text=input("Enter the string: ")
v, c=vowels_consonants(text)
print("VOWELS: ",v)
print("CONSONANTS: ",c)    