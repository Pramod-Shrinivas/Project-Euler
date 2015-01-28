#!/usr/bin/python
'''
    Purpose: https://projecteuler.net/problem=15
    @author:Pramod S
    Straight forward combinatorics approach
    In a 2x2 grid the number of paths needed to reach bottom right from top left is 4(doesnt matter how
    you take right or down). In other words out of 4 paths i have to choose 2 i.e: 4c2 = 6
    Similarly in 20x20 grid.. number of paths required to reach bottom right from top left is 40.
    Out of these 40, i have to choose 20 down paths(in other words same as 20 right paths) i.e: 40c20
'''
def fact(num):
    fact=1
    if num==0 or num==1:
        return 1
    for i in range(2,num+1):
        fact = fact*i
    return fact
        
def main():
    result = fact(40) / (fact(20) * fact(20))
    print(result)
    
if __name__ == "__main__":
    main()
