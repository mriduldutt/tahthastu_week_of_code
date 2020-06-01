n=int(input('Enter list size:-'))
print('Enter elements seprated by space :-')
list=list(map(int,input('Enter a elements').split()))
for j in range(len(list)-1):
    list[j]=max(list[j+1:])
print(list)
