
n=int(input('Enter list size :-'))
print('Enter list element seprated with A space')
l=list(map(int,input().split()))
l2=[]
for j in l:
    if j not in l2:
        l2.append(j)
print(l2)


 



    
        

