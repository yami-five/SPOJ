counter=int(input())
for j in range(counter):
    n,x,y=input().split()
    n=int(n)
    x=int(x)
    y=int(y)
    result=""
    for i in range(1,n):
        if i%x==0 and i%y!=0:
            result+=str(i)+' '
    print(result)
