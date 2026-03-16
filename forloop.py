for i in range (10):
    if i==5:
        continue
    print(i)
     
# for i in range (6):
#    if i==3:
#     continue
# print(i,"" ,i-=)

for i,j in zip(range(1,6),range (5,0,-1)):
    if i==3 and j==3:
        continue
    print(i, "", j)

