n=int(input())
for x in range(n):
    coords=input().split()
    try:
        A=(int(coords[3])-int(coords[1]))/(int(coords[2])-int(coords[0]))
        B=int(coords[1])-int(coords[0])*A
        if int(coords[5])==A*int(coords[4])+B:
           print("TAK")
        else:
           print("NIE")
    except ZeroDivisionError:
        print("TAK")
