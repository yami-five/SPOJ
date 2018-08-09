while True:
    try:
        C,word=input().split()
        print(word.replace(C,''))
    except EOFError:
        exit(0)
