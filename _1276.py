while True:
    try:
        words=input().split()
        line=""
        for x in range(len(words)):
            if x==0:
                line+=words[0]
            else:
                line+=words[x][0].upper()+words[x][1:]
        print(line)
    except EOFError:
        exit(0)
