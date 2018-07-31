counter=int(input())
for i in range(counter):
    pesel=input()
    sum=int(pesel[0])+int(pesel[1])*3+int(pesel[2])*7+int(pesel[3])*9
    sum+=int(pesel[4])+int(pesel[5])*3+int(pesel[6])*7+int(pesel[7])*9
    sum+=int(pesel[8])+int(pesel[9])*3+int(pesel[10])
    if sum>0:
        if sum%10==0:
            print('D')
        else:
            print('N')
    else:
        print('N')
