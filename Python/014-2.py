#!/usr/bin/python
'''
    Purpose: https://projecteuler.net/problem=14
    @author:Pramod S
    Caching in results
'''
def main():
    maxlength,limit,starting = 0,1000000,0
    cache = [-1]*(limit+1)
    cache[1]=1
    for i in range(2,limit+1):
        sequence=i
        k=0
        while(sequence!=1 and sequence>=i):
            k+=1
            if sequence%2==0: sequence = sequence/2
            else: sequence = sequence * 3 + 1
        cache[i] = k + (cache[int(sequence)])
        if(cache[i]>maxlength):
            maxlength=cache[i]
            starting=i
    print(starting)    
if __name__ == "__main__":
    main()
