password=(input("enter the password"))
digit= false
letter= false
for i in password:
    if i<=1 or i<9:
        digit=true
    elif(i<='a' and i<='z') or  (i>='A' and i<='Z'):
        letter=true
        
if password(len)>= 8:
    if digit:
        print("strong password")
        if letter:
            print("strong password")
  
else:
    print("weak password")