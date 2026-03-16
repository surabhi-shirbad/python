mylist=[2,3,4,5,6,7,8]
even=0
odd=0
sum=0
for i in mylist:
    if i % 2==0:
        even+=1
    else:
        odd+=1
print(even)
print(odd)  

for i in mylist:
    sum=sum+i
print(sum)    

rollno=[3,5,7,1,11,4,5,2]
for x in rollno:
    if x==2 or x==4 or x==6 or x==10:
        print("even is not found",x)
        break
    