#take two numbers if the products of the number is less that or equal to 1000 print the product else print the sum of number
a=int(input("enter a number"))
b=int(input("enter a number"))
if a*b<=1000:
    print(a*b)
else:
    print(a+b)
print("end")