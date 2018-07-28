def is_palindrome(num):
    if num==num[::-1]:
        return True
    else:
        return False

n=input()
for x in range(0,n):
    num=input()
    counter=0
    while is_palindrome(num)==False:
        counter+=1
        sum=0
        sum+=int(num)+int(num[::-1])
        num=str(sum)
    print(num,' ',counter)
