#!/usr/bin/python
'''
    Purpose: https://projecteuler.net/problem=14
    @author:Pramod S
    Direct Brute force Approach
'''
def main():
    maxlength,limit,starting = 0,1000000,0
    for i in range(2,limit+1):
        length=1
        sequence=i
        while(sequence!=1):
            if sequence%2==0: sequence = sequence/2
            else: sequence = sequence * 3 + 1
            length+=1
        if(length>maxlength):
            maxlength=length
            starting=i
    print(starting)    
if __name__ == "__main__":
    main()
