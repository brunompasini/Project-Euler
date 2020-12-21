from math import sqrt,ceil
import time
def num_divisors(n):
    div = 0
    for i in range(1,int(ceil(sqrt(n)))+1):
        if n%i==0:
            # n divisible by i means its also divisible by n/i
            div+=2
        if i*i == n:
            # unless its the sqrt, as i == n/i
            div-=1
    return div



def find_num(ndivs):
    ndv = 0
    i = 1
    tnum = 1
    while ndv <= ndivs:
        i += 1
        tnum += i
        ndv = num_divisors(tnum)
    return [tnum,ndv]

def main():
    start = time.time()
    print(find_num(500))
    end = time.time()
    print(end-start)

main()
# 76576500