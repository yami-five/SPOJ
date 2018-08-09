n,m=input().split()
m=int(m)
n=int(n)
lst=[[0]*m]*n
for x in range(n):
    lst[x]=input().split()
    
new_lst=[[0]*n]*m
    
for i in range(m):
    line=""
    for j in range(n):
        line+=lst[j][i]+' '
    print(line)
