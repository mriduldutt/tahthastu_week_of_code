n=int(input('Enter no houses:-'))
print('Enter houses val. seprated by space :-')
b=list(map(int,input('Enter values').split()))
sum=0
if(len(b)==1):
    sum=b[0]
for i in range(len(b)-1):
    if(i==0 and b[1]<b[0]):
        sum+=b[i]
    elif(b[i-1]<a[i] and b[i+1]<b[i]):
        sum+=b[i]
    elif(i==len(b)-2 and b[len(b)-1]>b[i]):
       sum+=b[i+1]
    
print('Maximum stolen value:',sum)
