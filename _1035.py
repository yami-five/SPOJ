while True:
    try:
        a,b,c=input().split()
        a=float(a)
        b=float(b)
        c=float(c)
        if (a+b>c) and (b+c>a) and (a+c>b) and a>0.0 and b>0.0 and c>0.0:
            print(1)
        else:
            print(0)
    except EOFError:
        exit(0)
