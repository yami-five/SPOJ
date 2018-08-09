chars=[]
n=int(input())
for x in range(n):
    line=input()
    for y in range(len(line)):
        char=line[y]
        if char in line[:y] or char==' ':
            pass
        elif char not in line[:y]:
            if x>0:
                for z in range(len(chars)+1):
                    if z==len(chars):
                        new=[char,line.count(char)]
                        chars.append(new)
                    elif char in chars[z]:
                        chars[z][1]=int(chars[z][1])+line.count(char)
                        break
            else:
                new=[char,line.count(char)]
                chars.append(new)
for x in range(97,123):
    for y in range(len(chars)):
        if ord(chars[y][0])==x:
            print(chars[y][0],' ',chars[y][1])
            chars.remove(chars[y])
            break
for x in range(65,91):
    for y in range(len(chars)):
        if ord(chars[y][0])==x:
            print(chars[y][0],' ',chars[y][1])
            chars.remove(chars[y])
            break
