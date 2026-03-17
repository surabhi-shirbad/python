#nested for loop
#i=1,j=1
#2
# for i in range (1,4):#outer
#     for j in range (1,4):#inner
#         print(i,end="")
#     print()    

# n= int(input("enter your number of rows"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(64+i),end="")
#     print()        


# n= int(input("enter your number of rows"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(n+1-i,end="")
#     print()
n= int(input("enter your number of rows"))
for i in range(1,n+1):
    for j in range(1,1+i):
        print(n+1-i,end="")
    print()        
                