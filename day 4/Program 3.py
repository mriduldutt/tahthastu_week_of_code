n=int(input('Enter the size of dictionary :-'))
dic={}
val1=val2=0
for i in range(n):
    key=int(input('Enter the '+str(i+1)+'key'))
    value=int(input('Enter the '+str(i+1)+'value'))
    dic[key]=value
    if(value>val1):
        val1=value



def secondmax(dic,val1):
    count=0
    val2=0
    for i in list(dic.keys()):
        if(dic[i]==val1):
            count+=1
        if(dic[i]==val1 and count==2):
            return val1

    for i in list(dic.keys()):
        if(dic[i]>val2 and dic[i] <val1):

            val2=dic[i]
            
    return(val2)

print(secondmax(dic,val1))







   

    

    

    

        



    

    

    

       

            count+=1

        if(dic[i]==value1 and count==2):

            return value1

    for i in list(dic.keys()):

        if(dic[i]>value2 and dic[i]<value1):

            value2=dic[i]

            

    return(value2)

print(second_max(dic,value1))
