#!/usr/bin/python
'''
    Purpose: https://projecteuler.net/problem=4  
    @author:Pramod S   
'''
def main():
    maxPalindrome=0
    for a in range(100,1000):
        for b in range(a+1,1000):
            prod=a*b
            if( (prod > maxPalindrome) & (str(prod) == str(prod)[::-1])):
               maxPalindrome=prod
    print("result {0}".format(maxPalindrome))
     
if __name__ == "__main__":
    main()
