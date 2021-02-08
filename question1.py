string = input("Enter a string:")
lower=upper=digit=schar=0;
for char in string:
    if char.islower():
        lower+=1
    elif char.isupper():
        upper+=1
    elif char.isdigit():
        digit+=1
    else:
        schar+=1
print("Lowercase:",lower,"Uppercase:",upper,"Digits:",digit,"schar:",schar)
    
        
