word=input("enter the word")
a='aeiou'
count=0
for i in word:
    if i in a:
        count +=1
print(count)