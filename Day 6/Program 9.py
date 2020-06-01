def kSmallest(ar,r,k):

    ar.sort() 
    return ar[k-1] 
if _name_=='_main_': 
    ar = [22, 13, 15, 17, 19] 
    r = len(ar) 
    k = 2
    print("K 's' th smallest element is", 
          kSmallest(arr, r, k))
