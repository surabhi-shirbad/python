mylist=[1,2,3,4,5]
def sum(mylist):
    sum=0
    for i in range(len(mylist)):
        sum=sum+mylist[i]
    return sum
res=sum(mylist)
print("result",res)