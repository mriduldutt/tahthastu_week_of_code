
n=int(input('Enter the elements.no :-'))
wl2=list(map(int,input('Enter seperate elements by space:-').split()))
odd=[]
even=[]
for i in wl2:
    if i%2==0:
       even.append(i) 
    else:
        odd.append(i)
finaly=sorted(odd)[::-1]
even=sorted(even)
for i in even:
    finaly.append(i)
print(finaly)
