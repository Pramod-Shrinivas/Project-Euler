#!/usr/bin/python
'''
    Purpose: https://projecteuler.net/problem=6

    The sum of all numbers from 1 to n is given by (n*(n+1))/2
    The sum of squares of numbers from 1 to n is given by (n*(n+1)*((2*n)+1))/6
    @author:Pramod S   
'''
def main():
    res = (100*101/2)*(100*101/2) - (100*101*201/6) 
    print("result {0}".format(res))
     
if __name__ == "__main__":
    main()
