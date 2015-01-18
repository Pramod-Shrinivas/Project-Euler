#!/usr/bin/python
'''
    Purpose: https://projecteuler.net/problem=9
    We know that a < b < c, a+b+c=1000 and a,b,c are integers implies: a is less than or equal to 333.
    Cause if a > 333 (if a=334) => b > 334 (b=335) and c > 335 (c=336) Clearly a + b + c > 1000. So a < 333.
    Again b + c < 1000 which => b < 500. Cause if say b=500, c >b => c=501(atleast) => b + c > 1000 !!!
    Hence a < 333 and b < 500, c = 1000-a-b 
    @author:Pramod S   
'''
def main():
    flag = 1
    for a in range(333):
        for b in range(500):
            c = 1000-a-b
            if(a*a + b*b == c*c):
                flag = 0
                break
        if(flag==0):
            break
    print("Pythagorean Triplet is {0} {1} {2}".format(a,b,c))
    print("Result {0}".format(a*b*c))
        
if __name__ == "__main__":
    main()
