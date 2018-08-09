while True:
    try:
        line=input()
        if line.count('>')>1 or line.count('<')>1:
            i,j=-1,0
            for x in range(len(line)):
                if line[x] is '>':
                    i=x+1
                elif line[x] is '<' and i>0:
                    j=x
                    break
            print(line[:i].upper()+line[i:j]+line[j:].upper())
        else:
            print(line.upper())
    except EOFError:
        exit(0)
