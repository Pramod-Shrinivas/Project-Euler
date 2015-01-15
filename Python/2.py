#!/usr/bin/python
'''
    Purpose: https://projecteuler.net/problem=2  
    @author:Pramod S   
'''
def main():
    f1,f2,sum=1,2,2
    while(f2<=4000000):
        f1,f2 = f2,f1+f2
        if(f2%2==0):
            sum+=f2
    print("result {0}".format(sum))
        
if __name__ == "__main__":
   main()
