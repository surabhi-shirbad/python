f_list1=['apple','ber=ry','cherry','papaya']
f_list2 = f_list1 #list1 ,2['apple','berry','cherry','papaya']
f_list3 = f_list1[:]#list3=['apple','berry','cherry','papaya']
f_list2[0]='guava'#list1,2#['guava','berry','cherry','papaya']
f_list3[1]='kiwi' #list3=['apple','berry','cherry','papaya']
sum=0
for ls in (f_list1,f_list2,f_list3):
    if ls[0]=='guava':
        sum+=1
    if ls[1]=='kiwi':  
        sum+=20
print(sum)      
 