from random import randint
primes=[2]
def is_prime(n):
    test=True
    for x in primes:
        if n%x==0:
            test=False
    return test
'''
'''
for x in range (2,20):
    if is_prime(x)==True:
        primes.append(x)
n=int(input(''))
for x in range(0,n):
    if int(input('')) in primes:
        print("TAK")
    else:
        print("NIE")
exit(0)
