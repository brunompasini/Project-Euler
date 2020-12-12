def is_prime(n):
    for k in range(2,n):
        if (n%k==0):
            return False
    return True

def lis_primes(size):
    primes = []
    n = 2
    while (len(primes) < size):
        if (is_prime(n)):
            primes.append(n)
        n+=1
    return primes[-1]

def main():
    print(lis_primes(10001))

main()
# 104743