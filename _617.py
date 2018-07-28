def merge(str1,str2):
    new_str=""
    if len(str1)>len(str2):
        n=len(str2)
    else:
        n=len(str1)
    for x in range(0,n):
        new_str+=str1[x]+str2[x]
    return new_str
n=int(input(''))
for x in range(0,n):
    str1,str2=input('').split(" ")
    print(merge(str1,str2))
