n=int(input(''))
def factorial_rest(n):
    if n<10:
        fac=1
        for y in range(1,n+1):
            fac*=y
        fac=str(fac)
        l=len(fac)
        if(l==1):
            print('0 ',fac[l-1])
        else:
            print(fac[l-2],' ',fac[l-1])
        return
    else:
        print('0 0')
        return
    
for x in range(0,n):
    factorial_rest(int(input()))

    
