list1=[11,12,13,43,32,76,75,87]
list2=[56,76,87,78,98,89,12,21]
list3=[]
for i in list1:
    if i%2!=0:
        list3.append(i)
for i in list2:
    if i%2==0:
        list3.append(i)
print(list3)
