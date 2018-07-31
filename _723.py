def ROL(array):
    temp=array[0]
    for x in range(0,len(array)-1):
        array[x]=array[x+1]
    array[len(array)-1]=temp

n=int(input(''))
for x in range(0,n):
    array=input('').split(" ")
    m=int(array[0])
    array=array[1:]
    for y in range(0,m+1):
        ROL(array)
    out=""
    for y in range(0,m):
        out+=array[y]+' '
    print(out)
