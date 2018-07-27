from math import pow
#from random import randint
def just_do_it(a,b):
    if len(b)==1:
       b=int(b[len(b)-1])
    else:
        b=int(str(b[len(b)-2]+b[len(b)-1]))
    a=int(a[len(a)-1])
    if a==5 or a==6 or b==1:
        print(a)
    elif b%4!=0:
        a=str(int(pow(a,b%4)))
        print(a[len(a)-1])
    else:
        a=str(int(pow(a,4)))
        print(a[len(a)-1])
    return
    
n=int(input(''))
#n=100
for x in range(0,n):
    a,b = input().split(" ")
    just_do_it(a,b)
    #just_do_it(str(randint(1,1000000001)),str(randint(1,1000000001)))
exit(0)
