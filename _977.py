lst=input().split()
result=""
for x in range(len(lst)-1,-1,-1):
    result+=lst[x]+' '
print(result)
