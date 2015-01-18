#!/usr/bin/python
from math import sqrt
'''
    Purpose: https://projecteuler.net/problem=7
    @author:Pramod S   
'''
def isPrime(num):
    flag=0
    for i in range(2,int(sqrt(num))):
        if(num%i==0):
            flag=1
            break
    if(flag==0 and num!=1):
        return num
    else:
        return 0
            
def main():
    count=1
    for i in range(3,200000,2):
        if(isPrime(i)):
            count+=1
        if(count==10001):
            break
    print("Result: {0}".format(i))    
     
if __name__ == "__main__":
    main()
