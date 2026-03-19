mylist=[]
sum=0
n = int(input("enter the number of n"))
for i in range(n):
    val = int(input("enter the val"))
    mylist.append(val)
print(mylist)        
for j in range(len(mylist)):
    if j+1 in range(len(mylist)):
        sum+=abs(mylist[j]-mylist[j+1])
print(sum)        
