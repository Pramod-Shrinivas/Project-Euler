#!/usr/bin/python
'''
    Purpose: https://projecteuler.net/problem=5  
    @author:Pramod S   
'''
def gcd(num1,num2):
    while(num2):
        num1,num2 = num2, num1 % num2
    return num1

def lcm(num1,num2):
    return num1 * num2 / gcd(num1,num2)
    
def main():
    res=1
    for i in range(11,21):
        res=lcm(res,i)
    print("result {0}".format(res))
     
if __name__ == "__main__":
    main()
