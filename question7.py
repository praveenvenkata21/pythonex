binary=input("Enter binary values:").split(',')
string=[]
for i in binary:
    dec=int(i,2)
    if dec%5==0:
        string.append(str(dec))
print(",".join(string))


        
