from random import randint
from math import gcd
import argparse as argp

def genPrimeList(n):
    primes = list()
    for num in range(3,n,2):
        if all(num%i!=0 for i in range(3,int(num**.5)+1, 2)):
            primes.append(num)
    return(primes)

def primRoots(n):
    coprime_set = {num for num in range(1, n) if gcd(num, n) == 1}
    roots = [g for g in range(n//2, n) if coprime_set == {pow(g, powers, n)
            for powers in range(1, n)}]
    return(roots[randint(0, len(roots)-1)])

def DH(primes, a=10000, b=100000):
    print('Generating primes...')
    primes = genPrimeList(primes)
    n = primes[randint(len(primes)//2, len(primes)-1)]
    print('Picking primitive root of n...')
    g = primRoots(n)
    prvA = randint(a, b)
    prvB = randint(a, b)
    X = pow(g, prvA, n)
    Y = pow(g, prvB, n)
    keyA = pow(Y, prvA, n)
    keyB = pow(X, prvB, n)
    print(f'n: {n}')
    print(f'g: {g}')
    print(f'Private key A: {prvA}')
    print(f'Private key B: {prvB}')
    print(f'X: {X}')
    print(f'Y: {Y}')
    print(f'Session keys A & B: {keyA}, {keyB}')
    
if (__name__ == '__main__'):
    parser = argp.ArgumentParser(description='Diffie-Hellman key exchange')
    parser.add_argument('prime', metavar='prime', type=int, help='Number to which generate primes')
    parser.add_argument('a', metavar='a', type=int, help='Random interval start')
    parser.add_argument('b', metavar='b', type=int, help='Random interval stop')

    args = parser.parse_args()
    
    DH(args.prime, args.a, args.b)