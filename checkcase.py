ch = ord(input("enter your ch"))
if ch>=65 and ch<=91:
    print("your entered character is in upper case")
elif ch>=97 and ch<=122:
    print("your entere character is in lower case")
elif ch>=48 and ch<=57:
    print("your entere character is in digit")
else:
    print("your entered character is in specail sysmbol")            