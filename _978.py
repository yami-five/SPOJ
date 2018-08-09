stack=[]
last_was_plus=False
while True:
    try:
        x=input()
        if last_was_plus==True and x not in ['+','-'] and x not in stack:
            stack=[x]+stack
            print(":)")
            last_was_plus=False
        elif x=='+':
            last_was_plus=True
        elif x=='-' and not not stack:
            print(stack[0])
            stack=stack[1:]
        else:
            print(":(")
    except EOFError:
        exit(0)
            
