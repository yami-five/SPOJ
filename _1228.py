from math import isclose
a,b,c=input().split()
a=float(a)
b=float(b)
c=float(c)
if ((c-b)<0.00 or (c-b)>0.00) and isclose(a,0.00):
    print("BR")
elif isclose((c-b),0.00) and isclose(a,0.00):
    print("NWR")
else:
    x=round((c-b)/a,2)
    if '.' not in str(x):
        print(str(x)+".00")
    elif str(x)[len(str(x))-2]=='.':
        print(str(x)+'0')
    else:
        print(str(x))
