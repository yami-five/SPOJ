while True:
    try:
        word=input()
        new_word=""
        for x in range(len(word)):
            if word[x]==' ':
                new_word+=' '
            elif word[x]=='Z':
                new_word+='C'
            elif word[x]=='Y':
                new_word+='B'
            elif word[x]=='X':
                new_word+='A'
            else:
                new_word+=chr(ord(word[x])+3)
        print(new_word)
    except EOFError:
        exit(0)
