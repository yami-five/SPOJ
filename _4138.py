n=int(input())
for i in range(n):
    c,k,w=input().split()
    c=int(c)
    k=int(k)
    w=int(w)
    if c*w>k:
        print("no")
    else:
        print("yes")
