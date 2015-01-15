#!/usr/bin/python
'''
    Purpose: https://projecteuler.net/problem=3  
    @author:Pramod S   
'''
def main():
    num,highestFactor,i = 600851475143,0,2
    while(num!=0):
        if((num%i)!=0):
            i+=1
        else:
            highestFactor = num
            num/=i
        if(num == 1):
            print("result {0}".format(highestFactor))
            break
    
if __name__ == "__main__":
   main()
    
