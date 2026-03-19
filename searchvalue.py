mylist=[4,5,3,2,7,9,0]
def searchValue(target):
    for i in range(len(mylist)):
        if mylist[i]==target:
            return target
        
    return -1

target=10
res=searchValue(target) 
if res!=-1:     
    print("value found on index value=",res)
else:
    print("value no found")    
