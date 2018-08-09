while True:
    try:
        print(input()[::-1])
    except EOFError:
        exit(0)
