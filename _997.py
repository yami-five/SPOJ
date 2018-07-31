while True:
    try:
        operation,a,b=input('').split(" ")
        a=int(a)
        b=int(b)
        if operation=='+':
            print(int(a+b))
        elif operation=='-':
            print(int(a-b))
        elif operation=='*':
            print(int(a*b))
        elif operation=='/':
            print(int(a/b))
        else:
            print(int(a%b))
    except EOFError:
        exit(0)
