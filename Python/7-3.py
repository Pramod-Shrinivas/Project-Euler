#!/usr/bin/python
'''
    Purpose: https://projecteuler.net/problem=7
    Sieve of Erasthonese Algorithm used. 
    Using enumerate() function. 
    Usage: enumerate(thing), where thing is either an iterator or a sequence, returns a iterator 
    that will return (0, thing[0]), (1, thing[1]), (2, thing[2]), and so forth
    Here we consider a list called primes of size 130000 which contains either true or false
    depending on whether the corresponding value is prime or not. Initialise primes list to true.
    primes[0] and primes[1] are set to none. cause 0 and 1 are not primes.
    On iterating we find primes[2] is true. Hence set all multiples of 2 to false and so on.
    We just look at 10001st item in the list primes having value true.
    @author:Pramod S   
'''
def main():
    primes = [True] * 130000
    primes[0],primes[1] = [None] * 2
    count =0
    for index,value in enumerate(primes):
        if value is True:
            primes[index*2::index] = [False] * ((129999//index) - 1)
            count+=1
        if count == 10001:
            print("Result {0}".format(index))
            break      
     
if __name__ == "__main__":
    main()
