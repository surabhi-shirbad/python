mydict ={
    101:"prashant",
    102:"ashish",
    "103":"mohit",
    "104":"trivani",
    101:"ashish",
    104:"ashish"
    }
print(mydict)

# for x in mydict:
#     print(x)

# for x in mydict.values():
#     print(x)

for x,y in mydict.items():
    print(x,y)

mydict["mobile_no"]=426536458763946
print(mydict)  

mydict.pop(103)  