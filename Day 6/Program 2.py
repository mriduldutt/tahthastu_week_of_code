def sort012( a, arrsize): 
    l = 0
    hi = arrsize - 1
    mid = 0
    while mid <= hi: 
        if a[mid] == 0: 
            a[l], a[mid] = a[mid], a[l] 
            l = l + 1
            mid = mid + 1
        elif a[mid] == 1: 
            mid = mid + 1
        else: 
            a[mid], a[hi] = a[hi], a[mid]  
            hi = hi - 1
    return a 
def printArray( a): 
    for k in a: 
        print k, 
arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1] 
arrsize = len(arr) 
arr = sort012( arr, arrsize) 
print "Array after segregation :\n", 
printArray(arr)
