def do_this_shit(word):
    result=""
    while word!="":
        x=word[0]
        counter=0
        while x==word[counter]:
            counter+=1
            if counter==len(word):
                break
        word=word[counter:]
        if counter==1:
            result+=x
        elif counter==2:
            result+=(2*x)
        else:
            result+=x+str(counter)
    return result
n=int(input(''))
for x in range(0,n):
    print(do_this_shit(input('')))
