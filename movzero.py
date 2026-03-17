myset={1,0,3,0,0,3,4,5,6}

for i in myset:
    if i==0:
        myset.remove(i)
        myset.append(i)
print(myset)
