def ROL(array,n):
    temp=array[0]
    for x in range(0,n-1):
        array[x]=array[x+1]
    array[len(array)-1]=temp

n,k=input().split()
n=int(n)
k=int(k)
array=input('').split(" ")
for x in range(0,k):
    ROL(array,n)
out=""
for y in range(0,n):
    out+=array[y]+' '
print(out)
