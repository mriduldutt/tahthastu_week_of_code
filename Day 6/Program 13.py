def solve(arr): 
    x = int(arr[0])
    y = int(arr[1])
    z = int(arr[2])
    
    for i in range(3,arr.size):
        if (x+y+z)>1 and (x+y+z)<2:
            print(x," ",y," ",z)
        if (x+y+z)>=2:
            if x>y and x>z:
                x=int(arr[i])
            else:
            if(y>x and y>z):
                y=int(arr[i])
            else:
                z=int(arr[i])
        else:
            if x<y && x<z :
                x=int(arr[i])
            else
            if y<x and y<z:
                y=int(arr[i])
            else:
                x=int(arr[i])
