password=(input("enter the password"))
digit= False
letter= False
for i in password:
    if i>='1' or i<='9':
        digit=True
    elif(i>='a' and i<='z') or  (i>='A' and i<='Z'):
        letter=True
        
if len(password)>= 8 and digit and letter:
    print("strong password")  
else:
    print("weak password")
    