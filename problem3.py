def is_prime(n):
    for k in range(2,n):
        if (n%k==0):
            return False
    return True

def factor(n):
    num = n
    m = 2
    al = []
    while (m <= n/2):
        if (is_prime(m) and num%m==0):
            num = num/m
            al.append(m)
        m+=1
        if num == 1:
            break
    return al[-1]

def main():
    print(factor(600851475143))

main()

# 6857