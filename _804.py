counter=int(input())
for i in range(counter):
    a,b=input().split()
    a=int(a)
    b=int(b)
    while a!=b:
        if a>b:
            a-=b
        else:
            b-=a
    print(a+b)
