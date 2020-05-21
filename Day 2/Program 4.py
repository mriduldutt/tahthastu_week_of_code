n=int(input("enter the no. :-"))
for i in range(n):
    print("*"*(n-i) + "  "*(i+1) + "*"*(n-i))
for i in range(2,n+1):
    print("*"*i + "  "*((n-i)+1) + "*"*i)
