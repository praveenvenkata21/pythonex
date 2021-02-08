string=input("Enter a string:")
lstring=""
ustring=""
for char in string:
    if char.islower():
        lstring+=char
    else:
        ustring+=char
lstring+=ustring
print(lstring)
        
