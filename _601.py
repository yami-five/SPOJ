def NWD(a,b):
    while b!=0:
        b,a=a%b,b
    return a

n=int(input(''))
for x in range(0,n):
    a,b=input('').split(" ")
    a=int(a)
    b=int(b)
    print(NWD(a,b))
