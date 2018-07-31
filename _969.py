while True:
    try:
        a,b,c=input().split()
        a=float(a)
        b=float(b)
        c=float(c)
        d=b*b-4*a*c
        if d>0:
            print(2)
        elif d<0:
            print(0)
        else:
            print(1)
    except EOFError:
        break
