counter=int(input())
for i in range(counter):
    numbers=input().split()
    x=int(numbers[0])
    result=""
    for j in range(2,x+1,2):
        result+=numbers[j]+' '
    for j in range(1,x+1,2):
        result+=numbers[j]+' '
    print(result)
        
        
