from random import randint
from math import gcd
import argparse as argp

def genPrimeList(n):
    primes = list()
    for num in range(3,n,2):
        if all(num%i!=0 for i in range(3,int(num**.5)+1, 2)):
            primes.append(num)
    return(primes)

def genPrime(primes):
    i = j = 0
    while (i == j):
        i = randint(len(primes)//2,len(primes)-1)
        j = randint(len(primes)//2,len(primes)-1)
    return(primes[i], primes[j])  

def genSinglePrime(primes, phi):
    i = 0
    while (True):
        i = randint(len(primes)//2,len(primes)-1)
        if (gcd(primes[i], phi) == 1):
            return(primes[i])
        
'''def genD(e, phi):
    while (True):
        d = randint(0, 1000000)
        if ((e*d-1)%phi == 0):
            return(d)'''
        
def generateKeys(n):
    print('Generating primes...')
    primes = genPrimeList(n)
    p, q = genPrime(primes)
    n = p * q
    phi = (p-1) * (q-1)
    print('Generating keys...')
    e = genSinglePrime(primes, phi)
    d = pow(e, -1, phi)                                #genD(e, phi)
    return ((e, n), (d, n))
    
if (__name__ == '__main__'):
    parser = argp.ArgumentParser(description='Generate a public and private RSA keys')
    parser.add_argument('prime', metavar='prime', type=int, help='Number to which generate primes')

    args = parser.parse_args()
    pubk, prvk = generateKeys(args.prime)
    print('Generated public key: {}'.format(pubk))
    print('Generated private key: {}'.format(prvk))