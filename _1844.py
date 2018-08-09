def ListToInt(lst):
    for x in range(len(lst)):
        lst[x]=int(lst[x])
    return lst

while True:
    try:
        lst=input().split()
        lst=ListToInt(lst)
        print(lst[2:].count(lst[0]))
    except EOFError:
        exit(0)
