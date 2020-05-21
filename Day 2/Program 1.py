
def even_odd(n):
    if(n%2==0):
        print("even no.")
    else:
        print("odd no.")
        
def prime_no(n):
    k=1
    for i in range(2,n):
        if(n%i==0):
            k = 0
            break
    if(k==0):
        print(" no. is not a prime number ")
    else:
        print("no. is prime")

def pallindrome(n):
    x = str(n)
    y = a[::-1]
    if(x==y):
        print("no. is palimdrome")
    else:
        print("no. is not palimdrome")

def armstrong(n):
    r = str(n)
    sum=0
    l =len(r)
    for i in r:
        sum +=int(i)**l
    if(n==sum):
        print("no. is armstrong")
    else:
        print("no. is not armstrong")
n=int(input('enter a no'))
even_odd(n)
prime_no(n)
pallindrome(n)
armstrong(n)
        
    
        



    
    
        
            
            
    
        
   
     



    
   
   
      
   
      



    
    
    
    
        
    
        
    
      







