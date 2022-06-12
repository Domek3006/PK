from random import randint
import argparse as argp

def genPrime(n):
    primes = list()
    for num in range(3,n,2):
        if all(num%i!=0 for i in range(3,int(num**.5)+1, 2)):
            primes.append(num)
    i = j = 0
    while (i == j):
        i = randint(len(primes)//2,len(primes)-1)
        j = randint(len(primes)//2,len(primes)-1)
        if(verify(primes[i], primes[j])):
            i = j
    return(primes[i], primes[j])

def verify(p, q):
    err = False
    if(p % 4 != 3):
        err = True
    if (q % 4 != 3):
        err = True
    return err

def genX(p, q, N):
    x = randint(1, N-1)
    while (x == p or x == q):
        x = randint(1, N-1)
    return x

def BBS(p, q, l):
    N = p * q
    x0 = genX(p, q, N)**2 % N
    print('p: {}; q: {}; x: {}'.format(p,q,x0))
    key = str(x0 % 2)
    for _ in range(l):
        x0 = x0**2 % N
        key += str(x0 % 2)
    print('key len: {}'.format(len(key)))
    return key
    
if __name__ == '__main__':
    parser = argp.ArgumentParser(description='Generate a psudorandom bit chain using Blum-Blum-Shub algorithm')
    parser.add_argument('prime', metavar='prime', type=int, help='Number to which generate primes')
    parser.add_argument('bits', metavar='bits', type=int, help='Number of bits to generate')

    args = parser.parse_args()
    with open('key.txt', 'w', encoding='utf-8') as key:
        p, q = genPrime(args.prime)
        key.write(BBS(p, q, args.bits-1))