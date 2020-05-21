f=int(input("enter the no.:-"))
a=0
b=1
print("fibbo series is :-",f,"the no. is following :-")
for i in range(f):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
