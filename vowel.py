v=['a','e','i','o','u']
w= input("enter the word where we we will search  the vowel:")
found=[]
for i in w:
    if i in v:
        if i not in found :
            found.append(i)
print('found vowel=',found) 
print('unique vowel',len (found), 'from the given word=',w)           