suma=0
while True:
    try:
        suma+=int(input(''))
        print(suma)
    except EOFError:
        exit(0)
