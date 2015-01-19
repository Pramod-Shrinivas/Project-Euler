#!/usr/bin/python
'''
    Purpose: https://projecteuler.net/problem=10
    Sieve of Erasthonese Algorithm used. Implemented using 007-3.py
    @author:Pramod S   
'''
def main():
    primes = [True] * 2000000
    primes[0],primes[1] = [None] * 2
    sum = 0
    for ind,val in enumerate(primes):
        if val is True and ind > 2000000 ** 0.5 + 1:
            sum += ind
        elif val is True:
            primes[ind*2::ind] = [False] * ((1999999//ind) - 1)
            sum += ind
    print("result: {0}".format(sum))

if __name__ == "__main__":
    main()
