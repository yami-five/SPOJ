n=int(input())
for x in range(n):
    counter=0
    num=int(input())
    counter=0
    while num!=1:
        if num%2==0:
            num/=2
        else:
            num=num*3+1
        counter+=1
    print(counter)
