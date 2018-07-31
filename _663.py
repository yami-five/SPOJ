from math import pow

def distance(n):
    points=[]
    for x in range(0,n):
        points.append(input('').split(" "))
        points[x].append(pow(pow(float(points[x][1]),2.0)+pow(float(points[x][2]),2.0),0.5))
    return points

def sort(points,n):
    for x in range(0,n):
        for y in range(0,n):
            if points[y][3]>points[x][3]:
                points[y],points[x]=points[x],points[y]
    return points

def write_list(points,n):
    for x in range(0,n):
        print(points[x][0],points[x][1],points[x][2])
    print('')

tests=int(input(''))
for x in range(0,tests):
    n=input('')
    while n=='':
        n=input('')
    n=int(n)
    points=distance(n)
    if n==1:
        write_list(points,n)
    else:
        points=sort(points,n)
        write_list(points,n)
