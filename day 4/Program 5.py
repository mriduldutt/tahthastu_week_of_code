
dic={}
n=int(input('Enter the votes no :-'))
for i in range(n):
    name=input('Name of candidate:-')
    if name not in list(dic.keys()):
        dic[name]=1
    else:
        dic[name]+=1
maxvotes=max(list(dic.values()))
maxvotescandidates=[]
for i in list(dic.keys()):
    if(dic[i]==maxvotes):
        maxvotescandidates.append(i)
print(min(maxvotescandidates))
        
