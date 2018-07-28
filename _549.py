def sum(m, lst):
    result=0
    for x in range(0,m):
        result+=int(lst[x])
    return result
n=int(input())
for x in range(0,n):
    m=int(input())
    lst=input().split(' ')
    print(sum(m, lst))
