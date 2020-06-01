
n=int(input('Enter the number :-'))

m=str(n)

new__s=''
for i in m:
    if i=='0':
        new__s+='5'
    else:
        new__s+=i

print(int(new__s))
