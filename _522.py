primes=[2,3,5,7,11,13,17,19,23,29]
def NWD(a,b):
    result=1
    for x in primes:
        if a%x==0 and b%x==0:
            result=x
    return result

def NWW(a,b):
    return a*b/NWD(a,b)

n=int(input(''))
for x in range(0,n):
    a,b=input('').split(" ")
    a=int(a)
    b=int(b)
    print(int(NWW(a,b)))
    
exit(0)
