string=input("Enter a string:")
count=0
j=-1
for i in range(0,len(string)):
        if string[i]!=string[j]:
            break
        else:
            count+=1
            j-=1
            
if count==len(string):
    print("Palindrome")
else:
    print("Not a Palindrome")
