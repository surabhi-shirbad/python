phy=int(input("enter marks of phy"))
math=int(input("enter marks of math"))
chem=int(input("enter marks of phy"))

total=phy+math+chem
percentage=(total/3)
print("total",total)
print("percentage",percentage)

if percentage>=60:
    print("eligible for placement")
else:
    print("not eligible")    
