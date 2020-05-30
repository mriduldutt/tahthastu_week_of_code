n = int(input("Enter the elements in 1 list:- "))
print("Enter the elements in 1 list :-")
listone = []
for i in range(n):
    listone.append(input())
m = int(input("Enter the elements in 2 list :-"))
print("Enter the elements in 2 list")
listtwo = []
for i in range(m):
    listtwo.append(input())
intersectionlist = list(set(listone).intersection(set(listtwo)))
print("The intersection of  1 list and 2 list is:", ", ".join(intersectionlist))
