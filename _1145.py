n=int(input())
for x in range(n):
    L,C=input().split()
    L=int(L)
    C=int(C)
    if L-1==0:
        print("TAK")
    elif C<(L-1):
        print("TAK")
    elif C%(L-1)!=0:
        print("TAK")
    elif C%(L-1)==0:
        print("NIE")
    else:
        print("NIE")
