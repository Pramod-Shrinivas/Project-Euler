#!/usr/bin/python
'''
    Purpose: https://projecteuler.net/problem=7
    Sieve of Erasthonese Algorithm used

    @author:Pramod S   
'''
def main():
    count=0
    multiples = set()
    for i in range(2,200000):
        if i not in multiples:
            count+=1
            if(count==10001):
                print("Result {0}".format(i))
            multiples.update(range(i*i,2000000,i))
     
if __name__ == "__main__":
    main()
