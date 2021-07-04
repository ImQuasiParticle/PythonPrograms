# Sieve of Eratosthenes Theory
# 0 1 2 3 4 5 6 7 8 9 10
# 11 12 13 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27 28 29 30
# 31 32 33 34 35 36 37 38 39 40
# 41 42 43 44 45 46 47 48 49 50
# Generating all prime number upto N with Time complexity of O(N*log(log N))

from math import *
def genPrime(n):
    primes = [True]*(n+1)
    primes[0] = False
    primes[1] = False
    for p in range(2,int(sqrt(n))+1):
        if primes[p] == True:
            for i in range(p*p,n+1,p): #range(start,end,increment's i by p )
                primes[i] = False
    
    for i in range(0,n+1):
        if primes[i] ==True:
            print(i)

t = int(input())
while t:
    n = int(input()) 
    genPrime(n)
    t-1

