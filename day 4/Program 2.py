n_list=int(input('Enter the size of tuple list'))
n_tuple=int(input('Enter the size of tuples'))
eclist=[]
for i in range(n_list):
    tup=tuple(map(int,input('Enter the element of tuple'+str(i+1)+' seprated by space:').split()))
    eclist.append(tup)
n=int(input('Enter index number of element about which you want to short list'))
for i in range(len(eclist)):
    for j in range(i+1,len(eclist)):
        if(eclist[i][n]>eclist[j][n]):
            eclist[i],eclist[j]=eclist[j],eclist[i]
print(eclist)







    

    





    

        

            

