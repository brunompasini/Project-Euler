def summ():
    n = 2**1000
    n = str(n)
    prod = 0
    for el in n:
        prod += int(el)
    return prod

def main():
    print(summ())

main()
# 1366