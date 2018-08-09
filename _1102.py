n=int(input())
for i in range(n):
    average=0
    numbers=input().split()
    counter=int(numbers[0])
    numbers=numbers[1:]
    for j in range(counter):
        average+=int(numbers[j])
    average/=counter
    dif=abs(average-int(numbers[0]))
    index=0
    for j in range(counter):
        if abs(average-int(numbers[j]))<dif:
            index=j
            dif=abs(average-int(numbers[j]))
    print(numbers[index])
    
