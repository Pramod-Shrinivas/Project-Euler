#!/usr/bin/python
'''
    Purpose: https://projecteuler.net/problem=1  
  
    The sum of all numbers from 1 to n is given by (n*(n+1))/2.
    Sum of all multiples of 3 is
        3 + 6 + 9 + ... + 996 + 999 = 3 * (1 + 2 + ... + 333) = 3 * (333*334)/2 
    Sum of all multiples of 5 is
        5 + 10 + 15 + ... + 995 = 5 * (1 + 2 + ... + 199) = 5 * (199*200)/2
    However adding the above would include sum of multiples of 15 twice. So we 
    have to delete an instance of sum of multiples of 15.
    Sum of all multiples of 15 is
        15 + 30 + ... + 990 = 15 * (1 + 2 + ... + 66) = 15 * (66*67)/2
    @author:Pramod S   
'''
def main():
    sum = ((3*333*334)/2) + ((5*199*200)/2) - ((15*66*67)/2)
    print("result {0}".format(sum))

if __name__ == "__main__":
   main()
