#!/usr/bin/python
'''
    Purpose: https://projecteuler.net/problem=7
    Sieve of Erasthonese Algorithm used. Implemented using 007-2.py
    @author:Pramod S   
'''
def main():
    sum=0
    multiples = set()
    for i in range(2,2000000):
        if i not in multiples:
            sum += i
            multiples.update(range(i*i,2000000,i))
    print("Result: {0}".format(sum))
     
if __name__ == "__main__":
    main()
