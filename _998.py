numbers=['0','0','0','0','0','0','0','0','0','0']
while True:
    try:
        operation,a,b=input().split()
        a=int(a)
        b=int(b)
        if operation=='z':
            numbers[a]=b
        elif operation=='+':
            print(int(numbers[a]+numbers[b]))
        elif operation=='-':
            print(int(numbers[a]-numbers[b]))
        elif operation=='*':
            print(int(numbers[a]*numbers[b]))
        elif operation=='/':
            print(int(numbers[a]/numbers[b]))
        else:
            print(int(numbers[a]%numbers[b]))
    except EOFError:
        exit(0)
