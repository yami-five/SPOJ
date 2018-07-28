from math import pow

def all_the_same(char,string):
    for x in string:
        if x!=char:
            return False
    return True
def float_to_hex(float_num):
    if float_num==0.0:
        return('0 0 0 0')
    binary=""
    sign='0'
    if float_num<0.0:
        sign='1'
    binary+=sign

    float_num=abs(float_num)
    exponent=255
    while float_num/pow(2,(exponent-127))>2.0 or float_num/pow(2,(exponent-127))<1.0:
        exponent-=1
    float_num=float_num/pow(2,(exponent-127))
    
    for x in range(7,-1,-1):
        if exponent-pow(2,x)>-1:
            binary+='1'
            exponent-=pow(2,x)
        else:
            binary+='0'

    float_num%=1.0
    divider=.5

    while float_num!=0.0:
        if float_num-divider>0 or float_num==divider:
            binary+='1'
            float_num-=divider
        else:
            binary+='0'
        divider/=2
    while len(binary)%4!=0:
        binary+='0'
    hexal=""
    while binary!="":
        hexal+=str(hex(int(binary[0:4],2)))[2:]
        binary=binary[4:]
    while len(hexal)<8:
        hexal+='0'
    space=2
    if len(hexal)>8:
        if hexal[6:8]=="ff":
            hexal=hexal[:6]
            hexal+="10"
        elif all_the_same(hexal[7],hexal[7:len(hexal)-1])==False:
            hexal=hexal[:8]
        else:
            hexal=hexal[:8]
            temp=hexal[7]
            hexal=hexal[:7]
            hexal+=str(hex(int('0x'+temp,0)+1))[2:]
    for x in range(0,3):
        hexal=hexal[:space]+' '+hexal[space:]
        space+=3
    for x in range(0,16):
        hexal=hexal.replace('0'+str(hex(x))[2:],str(hex(x))[2:])
    return(hexal)

n=int(input(''))
for x in range(0,n):
    print(float_to_hex(float(input(''))))

