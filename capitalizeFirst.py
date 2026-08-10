def captalizeFrist(arr):
    result=[]
    if len(arr)==0:
        return result
    result.append(arr[0][0].upper()+ arr[0][1:])
    return result+captalizeFrist(arr[1:])
print(captalizeFrist(["car",'taco','banana']))