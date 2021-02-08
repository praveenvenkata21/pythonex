num=input("Enter a number:")
size=len(num)
num=int(num)
temp=num
sum1=rem=0
while temp!=0:
    rem=temp%10
    sum1+=rem**size
    temp//=10
if sum1==num:
    print(num,"is a armstrong number")
else:
    print(num,"is not a armstrong number")
